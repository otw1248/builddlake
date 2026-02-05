#!/usr/bin/env python3
"""
Created by AI Assistant on 2026-02-05
Update stdHeaderUrl values in notice-details.json based on (id, noticeNo) pairs.
The input IDs are the actual 'id' field values in the JSON entries.
"""

import json
from pathlib import Path

# Mapping of (id, noticeNo) to new stdHeaderUrl values
URL_UPDATES = {
    (29, 1681): "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=2780C1AEFC6018AD7F6539C9FB27E621",
    (41, 1681): "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=2288632FCC8001A5B0B42E8A06C4D0E5",
    (42, 1681): "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=F7B125AAC6F2E6031D4C9BCEF3A57332",
    (43, 1681): "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=7DF6E86CCC44E0ACBEAD89B104DC5A11",
    (44, 1681): "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E628FC51036B2013AE6EAA546050C592",
    (45, 1681): "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=99BAB70DB4F556113DCEE25870D7BC62",
    (46, 1681): "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=2DB15E98AAB273A6E93A86DF2BCF304A",
    (4, 1742): "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=092E1EE1FFAD26436FEE322BB63C1807",
    (190, 1961): "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=1A5115036625EEEF42A44FF95604A725",
    (299, 2141): "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=1BDB880D4F5669045276B969DA2B12F2",
}

def update_std_header_urls(json_file_path):
    """Update stdHeaderUrl values in JSON file by id and noticeNo."""
    
    # Read the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated_count = 0
    not_found = []
    
    # Create a set of target (id, noticeNo) pairs that need to be found
    target_keys = set(URL_UPDATES.keys())
    found_keys = set()
    
    # Iterate through entries and update if matching (id, noticeNo)
    for entry in data:
        entry_id_str = entry.get('id', '')
        notice_no_str = entry.get('noticeNo', '')
        
        # Skip if either id or noticeNo is empty or not a valid integer
        if not entry_id_str or not notice_no_str:
            continue
        
        try:
            entry_id = int(entry_id_str)
            notice_no = int(notice_no_str)
        except ValueError:
            continue
        
        if (entry_id, notice_no) in URL_UPDATES:
            new_url = URL_UPDATES[(entry_id, notice_no)]
            old_url = entry.get('stdHeaderUrl', '')
            
            if old_url != new_url:
                entry['stdHeaderUrl'] = new_url
                updated_count += 1
                print(f"Updated ID {entry_id}, NoticeNo {notice_no}:")
                print(f"  Old: {old_url}")
                print(f"  New: {new_url}")
            else:
                print(f"Skipped ID {entry_id}, NoticeNo {notice_no}: URL already up to date")
            
            found_keys.add((entry_id, notice_no))
    
    # Check for any keys that weren't found
    not_found = list(target_keys - found_keys)
    
    # Write updated data back to the file
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total entries processed: {len(data)}")
    print(f"  Entries updated: {updated_count}")
    print(f"  Entries not found: {len(not_found)}")
    
    if not_found:
        print(f"\nNot found entries:")
        for entry_id, notice_no in not_found:
            print(f"  ID {entry_id}, NoticeNo {notice_no}")
    
    print(f"{'='*60}")
    print(f"File updated: {json_file_path}")

if __name__ == '__main__':
    script_dir = Path(__file__).parent
    json_file = script_dir / 'notice-details.json'
    
    if not json_file.exists():
        print(f"Error: File not found: {json_file}")
        exit(1)
    
    print(f"Updating stdHeaderUrl values in: {json_file}")
    print(f"Total updates to apply: {len(URL_UPDATES)}")
    print(f"{'='*60}\n")
    
    update_std_header_urls(json_file)
