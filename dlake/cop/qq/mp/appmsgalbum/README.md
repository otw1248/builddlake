# WeChat MP Album to Markdown Converter

Convert all articles from a WeChat Public Account album page to Markdown files.

## Overview

This tool fetches articles from a WeChat MP (公众号) album page (`mp.weixin.qq.com/mp/appmsgalbum`), converts each article's content to Markdown format, and saves them as `.md` files.

### Features

- **Full article collection**: Automatically paginates through the entire album (discovered 269 articles in the target album)
- **HTML to Markdown conversion**: Preserves article structure, lists, links, and formatting
- **Resume support**: Skips already-downloaded articles on re-run
- **Rate limiting**: Configurable delay between article fetches (default: 60 seconds)
- **Exception logging**: Detailed logs saved to `logs/` directory
- **Article index**: JSON index file (`article_index.json`) for quick reference

## Prerequisites

- Python 3.8+
- Dependencies: `requests`, `beautifulsoup4`, `html2text`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic (default album from Issue #9)

```bash
python3 appmsgalbum_to_md.py
```

### Custom album URL

```bash
python3 appmsgalbum_to_md.py --url "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=XXX&action=getalbum&album_id=YYY&scene=21#wechat_redirect"
```

### Limit number of articles (for testing)

```bash
# Download only the first 5 articles
python3 appmsgalbum_to_md.py --limit 5 --delay 10
```

### Custom output directory

```bash
python3 appmsgalbum_to_md.py --output /path/to/output
```

### All options

```
--url URL       WeChat MP Album page URL (default: the album from Issue #9)
--output DIR    Output directory for .md files (default: script directory)
--delay SECONDS Delay between article fetches in seconds (default: 60)
--limit N       Max number of articles to process (default: 0 = all)
```

## Output

### Generated files

| File | Description |
|------|-------------|
| `{pos}_{title}.md` | Converted Markdown article (e.g., `1_一天了解一家跨境支付公司：万里汇（WorldFirst）.md`) |
| `article_index.json` | JSON index with all article metadata (msgid, title, url, pos_num) |
| `logs/appmsgalbum_YYYYMMDD_HHMMSS.log` | Detailed execution log |

### Markdown file structure

Each `.md` file follows this format:

```markdown
# Article Title

**Author:** Author Name
**Date:** Publish Date
**Position:** 1
**Source:** Original URL

---

Article content converted to Markdown...
```

## How It Works

1. **Album pagination**: Fetches the initial album page (10 articles), then paginates using `begin_msgid` parameter until all articles are collected (269 total for the target album)
2. **Content extraction**: For each article, fetches the full article HTML and extracts content from the `#js_content` div
3. **CAPTCHA handling**: Uses complete article URLs (with `chksm` parameter) from `data-link` attributes to bypass WeChat's CAPTCHA verification
4. **Resume support**: Checks if `.md` file already exists before downloading, enabling incremental runs

## Tested Example

Successfully tested with the album from Issue #9:
- **Album**: "跨境支付公司" by "汇付通途" (269 articles)
- **Test**: Downloaded first 2 articles with `--limit 2 --delay 5`
- **Result**: Both articles converted successfully with proper formatting

## Notes

- WeChat may rate-limit or block if requests are too frequent. The default 60-second delay between articles is recommended
- Some articles may be behind a paywall and cannot be fetched
- If CAPTCHA is detected for an article, it is logged as an error and skipped
- The tool requires network access to `mp.weixin.qq.com`
