# Created by AI Assistant on 2026-02-05

import json
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

def extract_std_data(html):
    """
    Extract id, stdCode, stdHeaderUrl, and stdReleaseDate from the table rows.
    Table structure:
    - Column 1: 序号
    - Column 2: 标准号 - contains <a> tag with href (stdHeaderUrl) and text (stdCode)
    - Column 3: 中文名称
    - Column 4: 发布日期

    Returns a dictionary mapping id to a dict with stdHeaderUrl, stdCode, and stdReleaseDate.
    """
    soup = BeautifulSoup(html, 'html.parser')
    result = {}
    
    # Try to find table with class "table-striped"
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
            # Column 1 (index 0): ID (序号)
            record_id = tds[0].get_text(strip=True)
            # Column 2 (index 1): Standard code with link
            link = tds[1].find('a')
            if link:
                href = link.get('href', '')
                std_code = link.get_text(strip=True)
                # Column 4 (index 3): Release date
                std_release_date = tds[3].get_text(strip=True)
                result[record_id] = {
                    'stdCode': std_code,
                    'stdHeaderUrl': href,
                    'stdReleaseDate': std_release_date
                }
                print(f"  Extracted: id={record_id}, {std_code} -> {href} (Released: {std_release_date})")
    
    return result

def main():
    # File paths
    notice_details_path = '/workspace/dlake/gov/std/notice-details.json'
    target_url = 'https://openstd.samr.gov.cn/bzgk/gb/nd?no=2581'
    
    # Step 1: Fetch HTML content
    print(f"Fetching HTML from {target_url}...")
    html = fetch_html(target_url)
    if not html:
        print("Failed to fetch HTML. Exiting.")
        return
    
    # Step 2: Extract stdCode, stdHeaderUrl, and stdReleaseDate from table
    print("\nExtracting standard data from table...")
    std_data = extract_std_data(html)
    print(f"\nExtracted {len(std_data)} standard records")
    
    # Step 3: Load notice-details.json
    print(f"\nLoading {notice_details_path}...")
    notice_details = load_json_file(notice_details_path)
    
    # Step 4: Update records for noticeNo="2581"
    updated_count = 0
    for notice in notice_details:
        if notice.get('noticeNo') == '2581':
            record_id = notice.get('id', '')
            if record_id in std_data:
                old_code = notice.get('stdCode', '')
                old_url = notice.get('stdHeaderUrl', '')
                old_date = notice.get('stdReleaseDate', '')
                new_code = std_data[record_id]['stdCode']
                new_url = std_data[record_id]['stdHeaderUrl']
                new_date = std_data[record_id]['stdReleaseDate']
                
                # Update stdCode
                if old_code != new_code:
                    notice['stdCode'] = new_code
                    updated_count += 1
                    print(f"  Updated stdCode: id={record_id}")
                    print(f"    Old: {old_code}")
                    print(f"    New: {new_code}")
                
                # Update stdHeaderUrl
                if old_url != new_url:
                    notice['stdHeaderUrl'] = new_url
                    updated_count += 1
                    print(f"  Updated stdHeaderUrl: id={record_id}")
                    print(f"    Old: {old_url}")
                    print(f"    New: {new_url}")
                
                # Update stdReleaseDate
                if old_date != new_date:
                    notice['stdReleaseDate'] = new_date
                    updated_count += 1
                    print(f"  Updated stdReleaseDate: id={record_id}")
                    print(f"    Old: {old_date}")
                    print(f"    New: {new_date}")
            else:
                print(f"  Warning: No matching data found for id={record_id}")
    
    # Step 5: Save updated notice-details.json
    if updated_count > 0:
        print(f"\nSaving updated {notice_details_path}...")
        save_json_file(notice_details_path, notice_details)
        print(f"Completed. Updated {updated_count} fields.")
    else:
        print("\nNo records were updated.")

if __name__ == '__main__':
    main()
