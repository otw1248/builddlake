# Created by AI Assistant on 2026-02-05

import json
import re
from bs4 import BeautifulSoup
import requests

def load_json_file(filepath):
    """Load JSON file and return data."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(filepath, data):
    """Save data to JSON file with proper formatting."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def fetch_html(url):
    """Fetch HTML content from URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_href_links(html):
    """
    Extract href values from the table rows.
    Returns a dictionary mapping converted stdCode to stdHeaderUrl.
    The table shows: Original GB code -> Converted GB/T code (as link text)
    """
    soup = BeautifulSoup(html, 'html.parser')
    result = {}
    
    # Try to find table with class "table-striped" (added by JS)
    # Or find any table inside .content div (original structure)
    table = None
    
    # Method 1: Try to find table with class "table-striped"
    table = soup.find('table', class_='table-striped')
    
    # Method 2: If not found, look for table inside .content div
    if not table:
        content_div = soup.find('div', class_='content')
        if content_div:
            table = content_div.find('table')
    
    # Method 3: If still not found, look for any table in the document
    if not table:
        table = soup.find('table')
    
    if not table:
        print("Warning: table not found")
        return result
    
    # Iterate through table rows (skip header row)
    rows = table.find_all('tr')
    if len(rows) < 2:
        print("Warning: table has no data rows")
        return result
    
    for row in rows[1:]:  # Skip header row
        tds = row.find_all('td')
        if len(tds) >= 4:
            # Column 2 (index 1): Original standard code (e.g., "GB 10010-2009")
            # Column 4 (index 3): Link with converted standard code as text (e.g., "GB/T 10010-2009")
            link = tds[3].find('a')
            if link:
                href = link.get('href', '')
                # Use the link text as the key (the converted GB/T code)
                converted_std_code = link.get_text(strip=True)
                result[converted_std_code] = href
                print(f"  Extracted: {converted_std_code} -> {href}")
    
    return result

def main():
    # File paths
    notice_details_path = '/workspace/dlake/gov/std/notice-details.json'
    target_url = 'https://openstd.samr.gov.cn/bzgk/gb/nd?no=81'
    
    # Step 1: Fetch HTML content
    print(f"Fetching HTML from {target_url}...")
    html = fetch_html(target_url)
    if not html:
        print("Failed to fetch HTML. Exiting.")
        return
    
    # Step 2: Extract href links
    print("\nExtracting href links from table...")
    std_header_urls = extract_href_links(html)
    print(f"\nExtracted {len(std_header_urls)} stdHeaderUrl mappings")
    
    # Step 3: Load notice-details.json
    print(f"\nLoading {notice_details_path}...")
    notice_details = load_json_file(notice_details_path)
    
    # Step 4: Update stdHeaderUrl for noticeNo="81"
    updated_count = 0
    for notice in notice_details:
        if notice.get('noticeNo') == '81':
            std_code = notice.get('stdCode', '')
            if std_code in std_header_urls:
                old_url = notice.get('stdHeaderUrl', '')
                new_url = std_header_urls[std_code]
                if old_url != new_url:
                    notice['stdHeaderUrl'] = new_url
                    updated_count += 1
                    print(f"  Updated: {std_code}")
                    print(f"    Old: {old_url}")
                    print(f"    New: {new_url}")
                else:
                    print(f"  Skipped (no change): {std_code}")
            else:
                print(f"  Warning: No matching href found for {std_code}")
    
    # Step 5: Save updated notice-details.json
    if updated_count > 0:
        print(f"\nSaving updated {notice_details_path}...")
        save_json_file(notice_details_path, notice_details)
        print(f"Completed. Updated {updated_count} records.")
    else:
        print("\nNo records were updated.")

if __name__ == '__main__':
    main()
