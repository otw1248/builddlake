"""
Created by AI Assistant on 2026-02-05
Find items with empty or invalid stdNameEn or hcno fields
"""
import json
from typing import List, Dict


def load_std_code_ignore_list(meta_info_path: str) -> set:
    """Load stdCodeIgnoreList from the meta-info JSON file"""
    try:
        with open(meta_info_path, 'r', encoding='utf-8') as f:
            meta_data = json.load(f)
        ignore_list_str = meta_data.get('stdCodeIgnoreList', '')
        # Parse comma-separated values and strip whitespace
        ignore_list = [code.strip() for code in ignore_list_str.split(',') if code.strip()]
        return set(ignore_list)
    except Exception as e:
        print(f"Warning: Could not load stdCodeIgnoreList: {e}")
        return set()


def is_empty_or_short(value: any) -> bool:
    """Check if value is None, empty string, or length < 2"""
    if value is None:
        return True
    if not isinstance(value, str):
        return True
    if value.strip() == "":
        return True
    if len(value.strip()) < 2:
        return True
    return False


def find_invalid_items(json_file_path: str, ignore_std_codes: set) -> List[Dict]:
    """Find items where stdNameEn or hcno is empty or length < 2, ignoring specified stdCodes"""
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    invalid_items = []

    for idx, item in enumerate(data, start=1):
        # Skip items in the ignore list
        std_code = item.get('stdCode', '')
        if std_code in ignore_std_codes:
            continue
        issues = []

        # Check stdNameEn
        if is_empty_or_short(item.get('stdNameEn')):
            stdNameEn_value = item.get('stdNameEn')
            issues.append(f"stdNameEn is invalid: {repr(stdNameEn_value)}")

        # Check hcno
        if is_empty_or_short(item.get('hcno')):
            hcno_value = item.get('hcno')
            issues.append(f"hcno is invalid: {repr(hcno_value)}")

        if issues:
            invalid_items.append({
                'index': idx,
                'id': item.get('id'),
                'noticeNo': item.get('noticeNo'),
                'stdCode': item.get('stdCode'),
                'stdNameCn': item.get('stdNameCn'),
                'stdNameEn': item.get('stdNameEn'),
                'hcno': item.get('hcno'),
                'stdHeaderUrl': item.get('stdHeaderUrl'),
                'issues': issues
            })

    return invalid_items


def main():
    json_file = '/workspace/dlake/gov/std/notice-details.json'
    meta_info_file = '/workspace/dlake/gov/std/std-meta-info.json'
    output_file = '/workspace/dlake/gov/std/tocheck.txt'

    # Load stdCode ignore list
    ignore_std_codes = load_std_code_ignore_list(meta_info_file)
    print(f"Loaded {len(ignore_std_codes)} stdCode entries to ignore")

    print(f"\nScanning file: {json_file}\n")

    invalid_items = find_invalid_items(json_file, ignore_std_codes)

    # Write results to file
    with open(output_file, 'w', encoding='utf-8') as f:
        if invalid_items:
            f.write(f"Found {len(invalid_items)} items with invalid stdNameEn or hcno:\n\n")
            for item in invalid_items:
                f.write(f"[Index {item['index']}] ID: {item['id']}  noticeNo: {item['noticeNo']}\n")
                f.write(f"  stdCode: {item['stdCode']}\n")
                f.write(f"  stdNameCn: {item['stdNameCn']}\n")
                f.write(f"  stdNameEn: {item['stdNameEn']}\n")
                f.write(f"  hcno: {item['hcno']}\n")
                f.write(f"  stdHeaderUrl: {item['stdHeaderUrl']}\n")
                for issue in item['issues']:
                    f.write(f"  - {issue}\n")
                f.write("\n")
        else:
            f.write("No items with invalid stdNameEn or hcno found.\n")

    # Also print to console
    print(f"Results written to: {output_file}")
    if invalid_items:
        print(f"Found {len(invalid_items)} items with invalid stdNameEn or hcno")
    else:
        print("No items with invalid stdNameEn or hcno found.")


if __name__ == '__main__':
    main()
