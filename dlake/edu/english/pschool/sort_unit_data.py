"""
Created by AI Assistant on 2026-01-05
Script to sort unit-data.json by unit_id and appropriate ID fields
"""
import json
from pathlib import Path


def natural_sort_key(s):
    """
    Create a natural sort key for strings like '6-2-u1', '5-1-w-10', '1-1-w-001'
    """
    parts = []
    for part in s.split('-'):
        try:
            parts.append(int(part))
        except ValueError:
            parts.append(part.lower())
    return parts


def sort_items(items, id_field):
    """
    Sort items first by unit_id, then by the specified ID field
    """
    return sorted(items, key=lambda x: (
        natural_sort_key(x.get('unit_id', '')),
        natural_sort_key(x.get(id_field, ''))
    ))


def main():
    input_file = Path('/workspace/dlake/edu/english/pschool/unit-data.json')
    output_file = Path('/workspace/dlake/edu/english/pschool/unit-data-sorted.json')
    
    # Read the JSON file
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Sort each section
    result = {}
    
    if 'words' in data:
        print(f"Sorting {len(data['words'])} words...")
        result['words'] = sort_items(data['words'], 'word_id')
    
    if 'phrases' in data:
        print(f"Sorting {len(data['phrases'])} phrases...")
        result['phrases'] = sort_items(data['phrases'], 'phrase_id')
    
    if 'sentences' in data:
        print(f"Sorting {len(data['sentences'])} sentences...")
        result['sentences'] = sort_items(data['sentences'], 'sentence_id')
    
    # Preserve any other keys
    for key in data:
        if key not in result:
            result[key] = data[key]
    
    # Write the sorted data
    print(f"Writing sorted data to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print("Done!")


if __name__ == '__main__':
    main()
