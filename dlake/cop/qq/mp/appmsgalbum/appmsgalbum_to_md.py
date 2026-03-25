"""
Created by AI Assistant
Date: 2026-03-25

WeChat MP Album to Markdown converter.
Fetches all articles from a WeChat public account album page,
converts each article to Markdown format, and saves as .md files.

Usage:
    python3 appmsgalbum_to_md.py [--url URL] [--output DIR] [--delay SECONDS] [--limit N]

Example:
    python3 appmsgalbum_to_md.py --limit 2
"""

import argparse
import html
import json
import logging
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote

import html2text
import requests
from bs4 import BeautifulSoup

# --- Constants ---
DEFAULT_ALBUM_URL = (
    "https://mp.weixin.qq.com/mp/appmsgalbum"
    "?__biz=Mzk2NDcyNzExMQ==&action=getalbum"
    "&album_id=3948756631097098244&scene=21#wechat_redirect"
)
DEFAULT_OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DELAY = 60
PAGE_SIZE = 10
MAX_RETRIES = 3

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 "
        "MicroMessenger/8.0.43 NetType/WIFI"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Referer": "https://mp.weixin.qq.com/",
}

# --- Logging setup ---
def setup_logging(output_dir: str):
    """Configure logging to both file and console."""
    log_dir = os.path.join(output_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(
        log_dir,
        f"appmsgalbum_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.log",
    )
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    return log_file


logger = logging.getLogger(__name__)


# --- Album pagination ---
def parse_album_url(album_url: str) -> dict:
    """Extract biz, album_id, scene from the album URL."""
    parsed = urlparse(album_url)
    params = parse_qs(parsed.query)
    return {
        "biz": params.get("__biz", [""])[0],
        "album_id": params.get("album_id", [""])[0],
        "scene": params.get("scene", ["21"])[0],
    }


def fetch_album_page(url: str) -> str:
    """Fetch an album page with retries."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
            resp.encoding = "utf-8"
            return resp.text
        except Exception as e:
            logger.warning("Fetch attempt %d/%d failed for %s: %s", attempt, MAX_RETRIES, url[:80], e)
            if attempt < MAX_RETRIES:
                time.sleep(5 * attempt)
    raise RuntimeError("Failed to fetch album page after %d retries: %s" % (MAX_RETRIES, url[:80]))


def extract_articles_from_html(html_text: str) -> list:
    """Extract article info (pos_num, msgid, title, url) from album HTML."""
    soup = BeautifulSoup(html_text, "html.parser")
    li_items = soup.select("li.js_album_item")
    articles = []
    for li in li_items:
        articles.append({
            "pos_num": li.get("data-pos_num", ""),
            "msgid": li.get("data-msgid", ""),
            "title": li.get("data-title", ""),
            "url": li.get("data-link", ""),
        })
    return articles


def extract_continue_flag(html_text: str) -> bool:
    """Check if there are more older articles to load."""
    match = re.search(r"continue_flag\s*:\s*['\"]?(\d+)['\"]?", html_text)
    if match:
        return int(match.group(1)) == 1
    return False


def extract_album_meta(html_text: str) -> dict:
    """Extract album metadata from cgiData."""
    meta = {}
    patterns = {
        "albumId": r"albumId\s*:\s*['\"]?(\d+)['\"]?",
        "title": r"title\s*:\s*['\"]([^'\"]+)['\"]",
        "nick_name": r"nick_name\s*:\s*['\"]([^'\"]+)['\"]",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, html_text)
        if match:
            meta[key] = match.group(1)
    return meta


def get_all_article_urls(album_url: str) -> list:
    """Fetch all article URLs from the album using pagination.

    The album page renders 10 articles initially. Additional pages are
    loaded by requesting the same URL with begin_msgid and begin_itemidx
    parameters. Each HTML response contains <li> elements with data-link
    attributes that hold the full article URLs (including chksm param).
    """
    url_info = parse_album_url(album_url)
    logger.info(
        "Fetching album: biz=%s, album_id=%s, scene=%s",
        url_info["biz"], url_info["album_id"], url_info["scene"],
    )

    all_articles = []
    page_num = 0

    # Fetch initial page
    logger.info("Fetching page %d (initial)...", page_num + 1)
    html_text = fetch_album_page(album_url)

    # Log album metadata
    meta = extract_album_meta(html_text)
    if meta:
        logger.info("Album: %s by %s (id=%s)", meta.get("title"), meta.get("nick_name"), meta.get("albumId"))

    articles = extract_articles_from_html(html_text)
    all_articles.extend(articles)
    logger.info("  Got %d articles from initial page (total: %d)", len(articles), len(all_articles))
    page_num += 1

    # Paginate through remaining articles
    while extract_continue_flag(html_text):
        # Get the last article's msgid as the begin cursor
        last_article = articles[-1]
        last_msgid = last_article["msgid"]
        last_itemidx = "1"

        # Build pagination URL
        page_url = (
            "https://mp.weixin.qq.com/mp/appmsgalbum"
            "?__biz=%s&action=getalbum&album_id=%s&scene=126"
            "&begin_msgid=%s&begin_itemidx=%s&count=%d"
            % (url_info["biz"], url_info["album_id"], last_msgid, last_itemidx, PAGE_SIZE)
        )

        logger.info("Fetching page %d (begin_msgid=%s)...", page_num + 1, last_msgid)
        time.sleep(2)  # Small delay between page fetches
        html_text = fetch_album_page(page_url)
        articles = extract_articles_from_html(html_text)

        if not articles:
            logger.info("  No more articles returned, stopping.")
            break

        all_articles.extend(articles)
        logger.info("  Got %d articles (total: %d)", len(articles), len(all_articles))
        page_num += 1

    # Sort by pos_num (ascending: 1, 2, 3, ...)
    all_articles.sort(key=lambda a: int(a["pos_num"]) if a["pos_num"].isdigit() else 0)
    logger.info("Total articles collected: %d", len(all_articles))
    return all_articles


# --- Article fetching and conversion ---
def fetch_article(url: str) -> str:
    """Fetch an article page with retries."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
            resp.encoding = "utf-8"
            return resp.text
        except Exception as e:
            logger.warning("Article fetch attempt %d/%d failed: %s", attempt, MAX_RETRIES, e)
            if attempt < MAX_RETRIES:
                time.sleep(5 * attempt)
    raise RuntimeError("Failed to fetch article after %d retries: %s" % (MAX_RETRIES, url[:80]))


def extract_article_content(html_text: str) -> dict:
    """Extract title and content HTML from a WeChat article page."""
    soup = BeautifulSoup(html_text, "html.parser")

    # Extract title
    title_el = (
        soup.find("h1", id="activity-name")
        or soup.find("h1", class_="rich_media_title")
    )
    title = title_el.get_text(strip=True) if title_el else ""

    # Extract author
    author_el = soup.find("a", id="js_name") or soup.find("span", class_="rich_media_meta_text")
    author = author_el.get_text(strip=True) if author_el else ""

    # Extract date
    date_el = soup.find("em", id="publish_time")
    pub_date = date_el.get_text(strip=True) if date_el else ""

    # Extract content
    content_div = soup.select_one("#js_content")
    content_html = ""
    if content_div:
        content_html = str(content_div)
    else:
        logger.warning("Could not find #js_content in article page")

    return {
        "title": title,
        "author": author,
        "pub_date": pub_date,
        "content_html": content_html,
    }


def html_to_markdown(content_html: str) -> str:
    """Convert article content HTML to Markdown."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0  # No line wrapping
    h.unicode_snob = True
    h.skip_internal_links = True
    h.inline_links = True
    h.protect_links = True
    return h.handle(content_html)


def sanitize_filename(title: str, max_length: int = 80) -> str:
    """Convert title to a safe filename."""
    # Remove/replace invalid characters
    safe = re.sub(r'[\\/:*?"<>|\n\r\t]', '_', title)
    # Remove leading/trailing whitespace and dots
    safe = safe.strip('. ')
    # Truncate
    if len(safe) > max_length:
        safe = safe[:max_length].rstrip('. ')
    return safe if safe else "untitled"


def save_article_markdown(article_info: dict, markdown_content: str, output_dir: str) -> str:
    """Save article as a .md file. Returns the file path."""
    pos_num = article_info["pos_num"]
    title = article_info["title"]
    safe_title = sanitize_filename(title)
    filename = "%s_%s.md" % (pos_num, safe_title)
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    logger.info("Saved: %s", filename)
    return filepath


def build_article_markdown(article_info: dict, content: dict) -> str:
    """Build the complete markdown document for an article."""
    md_lines = []
    md_lines.append("# %s" % content["title"])
    md_lines.append("")
    if content["author"]:
        md_lines.append("**Author:** %s" % content["author"])
    if content["pub_date"]:
        md_lines.append("**Date:** %s" % content["pub_date"])
    md_lines.append("**Position:** %s" % article_info["pos_num"])
    md_lines.append("**Source:** %s" % article_info["url"])
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")

    body_md = html_to_markdown(content["content_html"])
    md_lines.append(body_md)
    md_lines.append("")
    return "\n".join(md_lines)


# --- Main pipeline ---
def process_album(album_url: str, output_dir: str, delay: int, limit: int = 0):
    """Main pipeline: fetch album articles and convert to markdown."""
    os.makedirs(output_dir, exist_ok=True)

    # Save article index as JSON for resume support
    index_file = os.path.join(output_dir, "article_index.json")
    existing_index = {}
    if os.path.exists(index_file):
        try:
            with open(index_file, "r", encoding="utf-8") as f:
                existing_index = json.load(f)
            logger.info("Loaded existing index with %d entries", len(existing_index))
        except Exception as e:
            logger.warning("Could not load existing index: %s", e)

    # Step 1: Get all article URLs
    logger.info("=" * 60)
    logger.info("Step 1: Collecting article URLs from album...")
    logger.info("=" * 60)
    all_articles = get_all_article_urls(album_url)

    # Step 2: Save article index (always save ALL articles for resume support)
    article_index = {}
    for art in all_articles:
        article_index[art["msgid"]] = art
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(article_index, f, ensure_ascii=False, indent=2)
    logger.info("Saved article index (%d entries) to %s", len(article_index), index_file)

    # Apply limit only to the download loop
    articles_to_process = all_articles[:limit] if limit > 0 else all_articles
    if limit > 0:
        logger.info("Limit applied: processing first %d articles (of %d total)", limit, len(all_articles))

    # Step 3: Fetch and convert each article
    logger.info("=" * 60)
    logger.info("Step 2: Fetching and converting articles to Markdown...")
    logger.info("=" * 60)

    success_count = 0
    skip_count = 0
    error_count = 0

    for i, article_info in enumerate(articles_to_process):
        pos_num = article_info["pos_num"]
        title = article_info["title"][:50]
        msgid = article_info["msgid"]
        safe_title = sanitize_filename(article_info["title"])
        filename = "%s_%s.md" % (pos_num, safe_title)
        filepath = os.path.join(output_dir, filename)

        logger.info(
            "[%d/%d] Processing #%s: %s...",
            i + 1, len(articles_to_process), pos_num, title,
        )

        # Skip if already downloaded
        if os.path.exists(filepath):
            logger.info("  Already exists, skipping.")
            skip_count += 1
            continue

        try:
            # Fetch article
            html_text = fetch_article(article_info["url"])

            # Check for CAPTCHA
            if "secitptpage" in html_text or "TCaptcha" in html_text:
                logger.error(
                    "  CAPTCHA detected for article #%s (msgid=%s). Skipping.",
                    pos_num, msgid,
                )
                error_count += 1
                continue

            # Extract content
            content = extract_article_content(html_text)
            if not content["content_html"]:
                logger.error(
                    "  No content found for article #%s (msgid=%s). Skipping.",
                    pos_num, msgid,
                )
                error_count += 1
                continue

            # Build and save markdown
            markdown_content = build_article_markdown(article_info, content)
            save_article_markdown(article_info, markdown_content, output_dir)
            success_count += 1

        except Exception as e:
            logger.error(
                "  Exception processing article #%s (msgid=%s): %s",
                pos_num, msgid, e,
                exc_info=True,
            )
            error_count += 1

        # Delay between articles (skip for the last one)
        if i < len(articles_to_process) - 1 and delay > 0:
            logger.info("  Waiting %d seconds before next article...", delay)
            time.sleep(delay)

    # Summary
    logger.info("=" * 60)
    logger.info("Done! Summary:")
    logger.info("  Total articles in album: %d", len(all_articles))
    logger.info("  Processed (with limit): %d", len(articles_to_process))
    logger.info("  Successfully converted: %d", success_count)
    logger.info("  Skipped (already exists): %d", skip_count)
    logger.info("  Errors: %d", error_count)
    logger.info("  Output directory: %s", output_dir)
    logger.info("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Convert WeChat MP Album articles to Markdown files.",
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_ALBUM_URL,
        help="WeChat MP Album page URL (default: the album from Issue #9)",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory for .md files (default: script directory)",
    )
    parser.add_argument(
        "--delay",
        type=int,
        default=DEFAULT_DELAY,
        help="Delay in seconds between article fetches (default: 60)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Max number of articles to process (default: 0 = all)",
    )
    args = parser.parse_args()

    log_file = setup_logging(args.output)
    logger.info("Log file: %s", log_file)
    logger.info("Album URL: %s", args.url)
    logger.info("Output dir: %s", args.output)
    logger.info("Delay: %ds, Limit: %d", args.delay, args.limit)

    process_album(args.url, args.output, args.delay, args.limit)


if __name__ == "__main__":
    main()
