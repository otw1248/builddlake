#!/usr/bin/env python3
"""
Created by AI Assistant on 2026-02-27
Remove duplicate entries from JSON based on langEn value
"""

import json
from pathlib import Path


def remove_duplicates(input_file: str, output_file: str = None) -> None:
    """
    Remove duplicate entries from JSON file based on langEn value.

    Args:
        input_file: Path to input JSON file
        output_file: Path to output JSON file (defaults to input_file)
    """
    input_path = Path(input_file)
    output_path = Path(output_file) if output_file else input_path

    # Read the JSON file
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Remove duplicates based on langEn (keep first occurrence)
    seen = set()
    unique_data = []
    duplicates_count = 0

    for item in data:
        lang_en = item.get('langEn')
        if lang_en not in seen:
            seen.add(lang_en)
            unique_data.append(item)
        else:
            duplicates_count += 1

    # Write the cleaned data
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(unique_data, f, ensure_ascii=False, indent=2)

    print(f"Original entries: {len(data)}")
    print(f"Removed duplicates: {duplicates_count}")
    print(f"Unique entries: {len(unique_data)}")
    print(f"Saved to: {output_path}")


if __name__ == '__main__':
    # Process the file in the same directory
    script_dir = Path(__file__).parent
    input_file = script_dir / 'feWords.json'

    # Optional: create backup before modifying
    backup_file = script_dir / 'feWords.backup.json'
    backup_file.write_text(input_file.read_text(encoding='utf-8'), encoding='utf-8')
    print(f"Backup created: {backup_file}\n")

    # Remove duplicates
    remove_duplicates(input_file)
