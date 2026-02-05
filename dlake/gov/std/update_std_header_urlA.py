# Created by AI Assistant on 2026-02-05

import json
import re
from bs4 import BeautifulSoup
import requests
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
        for attempt in range(3):
            try:
                response = requests.get(url, headers=headers, timeout=30)
                response.raise_for_status()
                response.encoding = 'utf-8'
                return response.text
            except Exception as e:
                print(f"Attempt {attempt + 1}/3 failed: {e}")
                if attempt < 2:
                    print(f"Waiting 10 seconds before retry...")
                    time.sleep(10)
                else:
                    print(f"All 3 attempts failed for {url}")
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
        return result
    
    # Extract stdCode from "标准号："
    # Pattern: 标准号：GB/T 12337-2014
    table = bor2_div.find('table', class_='tdlist')
    if table:
        # Look for h1 containing "标准号："
        h1_tag = bor2_div.find('h1')
        if h1_tag:
            h1_text = h1_tag.get_text(strip=True)
            if '标准号：' in h1_text:
                std_code_value = h1_text.replace('标准号：', '').strip()
                result['stdCode'] = std_code_value
        
        # Look for td containing "中文标准名称：" and "英文标准名称："
        for td in table.find_all('td'):
            text = td.get_text(strip=True)
            if text.startswith('中文标准名称：'):
                # Extract text after the colon
                chinese_name = text.replace('中文标准名称：', '').strip()
                # Remove any <b> tags formatting
                b_tag = td.find('b')
                if b_tag:
                    chinese_name = b_tag.get_text(strip=True)
                result['stdNameCn'] = chinese_name
            if text.startswith('英文标准名称：'):
                # Extract text after the colon
                english_name = text.replace('英文标准名称：', '').strip()
                # Remove any <b> tags formatting
                b_tag = td.find('b')
                if b_tag:
                    english_name = b_tag.get_text(strip=True)
                result['stdNameEn'] = english_name
    
    # Extract hcno from data-value attribute in buttons
    buttons = bor2_div.find_all('button')
    for button in buttons:
        data_value = button.get('data-value')
        if data_value:
            result['hcno'] = data_value
            break
    
    return result

def main():
    # File paths
    notice_details_path = '/workspace/dlake/gov/std/notice-details.json'
    std_meta_info_path = '/workspace/dlake/gov/std/std-meta-info.json'
     
    # Step 1: Read std-meta-info.json to get ignore list
    print("Loading std-meta-info.json...")
    std_meta_info = load_json_file(std_meta_info_path)
    ignore_list_str = std_meta_info.get('stdCodeIgnoreList', '')
    ignore_list = set([code.strip() for code in ignore_list_str.split(',') if code.strip()])
    print(f"Ignore list contains {len(ignore_list)} stdCodes")

    # Step 2: Read notice-details.json
    print("Loading notice-details.json...")
    notice_details = load_json_file(notice_details_path)
    
    # Step 3: Find items with stdHeaderUrl, id, noticeNo not empty, but stdCode or stdNameCn or stdNameEn or hcno is empty
    # Skip items whose stdCode is in the ignore list
    items_to_update = []
    for item in notice_details:
        std_header_url = item.get('stdHeaderUrl', '')
        id_value = item.get('id', '')
        notice_no = item.get('noticeNo', '')
        std_code = item.get('stdCode', '')
        
        # Check if stdHeaderUrl, id, noticeNo are not empty
        if std_header_url and id_value and notice_no:
            # Check if any of stdCode, stdNameCn, stdNameEn, hcno is empty
            # Also skip if stdCode is in the ignore list
            if std_code in ignore_list:
                print(f"Skipping {std_code} (in ignore list)")
            elif (not std_code or not item.get('stdNameCn') or 
                not item.get('stdNameEn') or not item.get('hcno')):
                items_to_update.append(item)
    
    print(f"Found {len(items_to_update)} items to update")
    
    # Step 4: Update each item
    updated_count = 0
    for item in items_to_update:
        std_header_url = item.get('stdHeaderUrl', '')
        id_value = item.get('id', '')
        notice_no = item.get('noticeNo', '')
        std_code = item.get('stdCode', '')
        
        print(f"\nProcessing: id={id_value}, noticeNo={notice_no}, stdCode={std_code}")
        print(f"  URL: {std_header_url}")
        
        # Fetch HTML from stdHeaderUrl
        html = fetch_html(std_header_url)
        if not html:
            print(f"  Failed to fetch HTML for id={id_value}, noticeNo={notice_no}")
            continue
        
        # Parse HTML to extract header info
        header_info = parse_std_header(html, std_code, std_header_url)
        
        if header_info:
            print(f"  Extracted: {header_info}")
            
            # Update item with extracted info only if the field is empty
            if not item.get('stdCode') and header_info.get('stdCode'):
                item['stdCode'] = header_info['stdCode']
            if not item.get('stdNameCn') and header_info.get('stdNameCn'):
                item['stdNameCn'] = header_info['stdNameCn']
            if not item.get('stdNameEn') and header_info.get('stdNameEn'):
                item['stdNameEn'] = header_info['stdNameEn']
            if not item.get('hcno') and header_info.get('hcno'):
                item['hcno'] = header_info['hcno']
            
            updated_count += 1
            
            # Save updated notice-details.json after each successful update
            save_json_file(notice_details_path, notice_details)
            print(f"  Updated and saved (total updated: {updated_count})")
            
            # Wait random time before next request to avoid rate limiting
            wait_time = 3 + random.randint(1, 6)
            print(f"  Waiting {wait_time} seconds before next request...")
            time.sleep(wait_time)
        else:
            print(f"  No header info extracted from HTML")
    
    print(f"\nCompleted. Total updated: {updated_count}")

if __name__ == '__main__':
    main()
