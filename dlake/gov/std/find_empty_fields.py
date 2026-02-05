"""
Created by AI Assistant on 2026-02-05
Find items with empty or invalid stdNameEn or hcno fields
"""
import json
from typing import List, Dict


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


def find_invalid_items(json_file_path: str) -> List[Dict]:
    """Find items where stdNameEn or hcno is empty or length < 2"""
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    invalid_items = []

    for idx, item in enumerate(data, start=1):
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
    output_file = '/workspace/dlake/gov/std/tocheck.txt'

    print(f"Scanning file: {json_file}\n")

    invalid_items = find_invalid_items(json_file)

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
