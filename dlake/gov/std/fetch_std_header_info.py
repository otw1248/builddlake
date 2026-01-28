# Created by AI Assistant on 2026-01-28

import json
import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import time
import random

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
        for attempt in range(5):
            try:
                response = requests.get(url, headers=headers, timeout=30)
                response.raise_for_status()
                response.encoding = 'utf-8'
                return response.text
            except Exception as e:
                print(f"Attempt {attempt + 1}/5 failed: {e}")
                if attempt < 4:
                    print(f"Waiting 30 seconds before retry...")
                    time.sleep(30)
                else:
                    print(f"All 5 attempts failed for {url}")
                    raise
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_std_header(html, std_code, std_header_url):
    """Parse standard header information from HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    result = {}
    
    # Find the div with class "bor2"
    bor2_div = soup.find('div', class_='bor2')
    if not bor2_div:
        print("Warning: div with class 'bor2' not found")
        # Write to tocheck.txt
        with open('/workspace/dlake/gov/std/tocheck.txt', 'a', encoding='utf-8') as f:
            f.write(f"{std_code}\t{std_header_url}\n")
        return result
    
    # Extract English standard name from "英文标准名称："
    # Pattern: 英文标准名称：<b>Safety protection specification for...</b>
    table = bor2_div.find('table', class_='tdlist')
    if table:
        # Look for td containing "英文标准名称："
        for td in table.find_all('td'):
            text = td.get_text(strip=True)
            if text.startswith('英文标准名称：'):
                # Extract text after the colon
                english_name = text.replace('英文标准名称：', '').strip()
                # Remove any <b> tags formatting
                b_tag = td.find('b')
                if b_tag:
                    english_name = b_tag.get_text(strip=True)
                result['stdNameEn'] = english_name
                break
    
    # Extract hcno from data-value attribute in buttons
    buttons = bor2_div.find_all('button')
    for button in buttons:
        data_value = button.get('data-value')
        if data_value:
            result['hcno'] = data_value
            break
    
    # Find CCS value (中国标准分类号)
    # Pattern: div with title "中国标准分类号（CCS）" followed by content div with value
    # Note: HTML may have typo 'clsss="row"' instead of 'class="row"'
    rows = []
    for div in bor2_div.find_all('div'):
        # Check if div has class or clsss attribute containing 'row'
        classes = div.get('class', [])
        clsss = div.get('clsss', [])
        if 'row' in classes or 'row' in clsss:
            rows.append(div)
    
    for row in rows:
        titles = row.find_all('div', class_='title')
        contents = row.find_all('div', class_='content')
        
        for i, title in enumerate(titles):
            title_text = title.get_text(strip=True)
            if '中国标准分类号（CCS）' in title_text and i < len(contents):
                result['cssValue'] = contents[i].get_text(strip=True)
            if '国际标准分类号（ICS）' in title_text and i < len(contents):
                result['icsValue'] = contents[i].get_text(strip=True)
            if '主管部门' in title_text and i < len(contents):
                result['competentDepartment'] = contents[i].get_text(strip=True)
    
    return result

def main():
    # File paths
    notice_details_path = '/workspace/dlake/gov/std/notice-details.json'
    meta_info_path = '/workspace/dlake/gov/std/std-meta-info.json'
    
    # Step 1: Read notice-details.json
    print("Loading notice-details.json...")
    notice_details = load_json_file(notice_details_path)
    
    # Sort noticeDetailItem list by noticeNo asc, id asc
    sorted_notices = sorted(
        notice_details,
        key=lambda x: (int(x.get('noticeNo', '0') or '0'), int(x.get('id', '0') or '0'))
    )
    print(f"Total notices: {len(sorted_notices)}")
    
    # Step 2: Read std-meta-info.json
    print("Loading std-meta-info.json...")
    meta_info = load_json_file(meta_info_path)
    
    notice_no_cursor_from_detail = meta_info.get('noticeNoCursorFromDetail', '')
    std_code_cursor = meta_info.get('stdCodeCursor', '')
    std_code_already_fetched_list = set(meta_info.get('stdCodeAlreadyFetchedList', '').split(',')) if meta_info.get('stdCodeAlreadyFetchedList') else set()
    std_code_ignore_list = set(meta_info.get('stdCodeIgnoreList', '').split(',')) if meta_info.get('stdCodeIgnoreList') else set()
    
    # Filter out empty strings from sets
    std_code_already_fetched_list.discard('')
    std_code_ignore_list.discard('')
    
    print(f"Already fetched: {len(std_code_already_fetched_list)}, Ignored: {len(std_code_ignore_list)}")
    
    # Step 3: Loop through noticeDetailItem list
    updated_count = 0
    for notice in sorted_notices:
        # Limit to 10 updates per run
        if updated_count >= 200:
            print(f"\nReached limit of 200 updates. Stopping.")
            break
        std_code = notice.get('stdCode', '')
        
        # Skip if already fetched or ignored
        if std_code in std_code_already_fetched_list:
            continue
        if std_code in std_code_ignore_list:
            continue
        
        # Set cursor values
        notice_no = notice.get('noticeNo', '')
        meta_info['noticeNoCursorFromDetail'] = notice_no
        meta_info['stdCodeCursor'] = std_code
        

        
        # Fetch HTML from stdHeaderUrl
        std_header_url = notice.get('stdHeaderUrl', '')

        # Print progress
        print(f"\nProcessing: {std_code} (noticeNo: {notice_no}, url: {std_header_url})")

        if not std_header_url:
            print(f"  No stdHeaderUrl found for {std_code}")
            continue
        
        html = fetch_html(std_header_url)
        if not html:
            print(f"  Failed to fetch HTML for {std_code}")
            
            # Write to tocheck.txt
            with open('/workspace/dlake/gov/std/tocheck.txt', 'a', encoding='utf-8') as f:
                f.write(f"{std_code}\t{std_header_url}\n")
            continue
        
        # Parse HTML to extract header info
        header_info = parse_std_header(html, std_code, std_header_url)
        
        if header_info:
            print(f"  Extracted: {header_info}")
            
            # Update notice with extracted info
            notice.update(header_info)
            
            # Mark as fetched
            std_code_already_fetched_list.add(std_code)
            updated_count += 1
            
            # Save meta-info after each successful fetch
            meta_info['stdCodeAlreadyFetchedList'] = ','.join(sorted(std_code_already_fetched_list))
            save_json_file(meta_info_path, meta_info)
            
            # Save updated notice-details.json
            save_json_file(notice_details_path, sorted_notices)
            
            print(f"  Updated and saved (total updated: {updated_count})")
            
            # Wait 30 + random(1-60) seconds before next request
            wait_time = 10 + random.randint(1, 30)
            print(f"  Waiting {wait_time} seconds before next request...")
            time.sleep(wait_time)
        else:
            print(f"  No header info extracted from HTML")
    
    # Final save
    save_json_file(meta_info_path, meta_info)
    save_json_file(notice_details_path, sorted_notices)
    
    print(f"\nCompleted. Total updated: {updated_count}")
    print(f"Meta-info saved with cursor: noticeNo={meta_info['noticeNoCursorFromDetail']}, stdCode={meta_info['stdCodeCursor']}")

if __name__ == '__main__':
    main()
