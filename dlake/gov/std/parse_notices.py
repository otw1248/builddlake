"""
Created by AI Assistant
Date: 2026-01-26
"""

import json
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from pathlib import Path


def parse_notice_item(element):
    """Parse a single notice item from HTML element"""
    result = {}
    
    # Extract id from href
    href = element.get('href', '')
    id_match = re.search(r"searchN\('(\d+)'\)", href)
    if id_match:
        result['id'] = id_match.group(1)
    
    # Extract title (text before span)
    # Get all content, then extract title part
    text_content = element.get_text(strip=True)
    span_element = element.find('span')
    if span_element:
        title = span_element.previous_sibling.strip()
        result['title'] = title
        
        # Extract date from span
        date_text = span_element.get_text(strip=True)
        result['date'] = date_text
    else:
        result['title'] = text_content
    
    return result


def fetch_notices(config_path, latest_notice_id=None):
    """Fetch notices from the configured source URL"""
    # Read configuration
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # Use noticeSourceUrl2 if latest_notice_id exists
    if latest_notice_id:
        base_url = config.get('noticeSourceUrl2', config['noticeSourceUrl'])
    else:
        base_url = config['noticeSourceUrl']

    page_param = config.get('pageParam', {})
    
    # Determine page range
    page_name = page_param.get('name', 'page')
    min_page = page_param.get('minValue', 1)
    max_page = page_param.get('maxValue', 1)
    
    all_notices = []
    should_stop = False  # Flag to stop fetching more pages

    # Iterate through all pages
    for page in range(min_page, max_page + 1):
        if should_stop:
            print(f"Stopping at page {page} as latest notice id reached")
            break

        # Replace page placeholder with actual value
        url = base_url.replace(f'{{{page_name}}}', str(page))

        print(f"Fetching page {page}: {url}")

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            response.encoding = 'utf-8'

            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all notice items
            selector = config['noticeItem']['selector']
            notice_elements = soup.select(selector)

            print(f"  Found {len(notice_elements)} notices")

            # Parse each notice
            for element in notice_elements:
                notice = parse_notice_item(element)
                if notice:
                    # Skip if id is less than or equal to latest_notice_id
                    if latest_notice_id:
                        if int(notice['id']) <= int(latest_notice_id):
                            print(f"  Found notice with id {notice['id']} <= latest_notice_id {latest_notice_id}, stopping pagination")
                            should_stop = True
                            break
                    notice['page'] = page
                    all_notices.append(notice)
                    
        except requests.RequestException as e:
            print(f"  Error fetching page {page}: {e}")
            continue
    
    return all_notices


def get_latest_notice_item(output_path):
    """Get the first (latest) notice item from existing JSON file"""
    try:
        if output_path.exists():
            with open(output_path, 'r', encoding='utf-8') as f:
                notices = json.load(f)
                if notices and len(notices) > 0:
                    return notices[0]
    except Exception as e:
        print(f"Warning: Could not read existing notices: {e}")
    return None


def save_notices(notices, output_path):
    """Save notices to JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notices, f, ensure_ascii=False, indent=2)

    print(f"\nSaved {len(notices)} notices to {output_path}")


def main():
    """Main execution function"""
    # Get configuration file path
    script_dir = Path(__file__).parent
    config_path = script_dir / 'cn-gov-std.json'

    # Output file path
    output_path = script_dir / 'notices.json'

    # Get latest notice id from existing file
    latest_notice_item = get_latest_notice_item(output_path)
    latest_notice_id = latest_notice_item['id'] if latest_notice_item else None

    # Fetch notices (with optional latest_notice_id for incremental updates)
    notices = fetch_notices(config_path, latest_notice_id)

    # Save to JSON
    if notices:
        # If existing file exists, merge new items at the beginning
        if latest_notice_item:
            with open(output_path, 'r', encoding='utf-8') as f:
                existing_notices = json.load(f)
            merged_notices = notices + existing_notices
            save_notices(merged_notices, output_path)
        else:
            save_notices(notices, output_path)
    else:
        print("No notices found.")


if __name__ == '__main__':
    main()
