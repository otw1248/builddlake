#!/usr/bin/env python3
"""
Split Oxford Dictionary JSON file by alphabet
Created by AI Assistant on 2026-01-19
"""

import json
import os
from collections import defaultdict


def split_json_by_alphabet(input_file, output_dir):
    """Split JSON dictionary entries into separate files by alphabet."""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the large JSON file
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    entries = data.get('entries', [])
    total_entries = len(entries)
    print(f"Total entries: {total_entries}")
    
    # Group entries by first letter
    alphabet_groups = defaultdict(list)
    
    for entry in entries:
        word = entry.get('word', '')
        if word:
            first_char = word[0].upper()
            alphabet_groups[first_char].append(entry)
    
    print(f"Found {len(alphabet_groups)} alphabet groups")
    
    # Write each group to a separate JSON file
    total_written = 0
    for char in sorted(alphabet_groups.keys()):
        group_entries = alphabet_groups[char]
        
        # Create output data structure
        output_data = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": f"Oxford English Dictionary - {char}",
            "total_entries": len(group_entries),
            "entries": group_entries
        }
        
        # Write to file
        output_file = os.path.join(output_dir, f"OxfordDict_{char}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        print(f"Written {len(group_entries)} entries to {output_file}")
        total_written += len(group_entries)
    
    print(f"\nCompleted! Total entries written: {total_written}")
    print(f"Output directory: {output_dir}")


if __name__ == "__main__":
    input_file = "/workspace/dlake/edu/english/oxford/OxfordDict.json"
    output_dir = "/workspace/dlake/edu/english/oxford"
    
    split_json_by_alphabet(input_file, output_dir)
