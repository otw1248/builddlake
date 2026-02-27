# Created by AI Assistant on 2026-02-27

import json
import sys

def sort_json_by_lang_en(input_file, output_file=None):
    """
    Sort JSON file based on langEn field.
    
    Args:
        input_file: Path to input JSON file
        output_file: Path to output JSON file (optional, defaults to input_file)
    """
    # Read the JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Sort the data by langEn field (case-insensitive)
    sorted_data = sorted(data, key=lambda x: x['langEn'].lower())
    
    # Determine output file
    if output_file is None:
        output_file = input_file
    
    # Write the sorted data back to file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully sorted {len(sorted_data)} entries by langEn")
    print(f"Output written to: {output_file}")

if __name__ == '__main__':
    # Use the file in the current directory
    input_file = 'feWords.json'
    output_file = 'feWords_sorted.json'  # Create a new file instead of overwriting
    
    # Allow command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    sort_json_by_lang_en(input_file, output_file)
