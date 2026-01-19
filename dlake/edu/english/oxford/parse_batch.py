# Created by AI Assistant on 2026-01-19
"""
Parse dictionary in batches to handle large file
"""

from oxford_parser import OxfordDictionaryParser
import json

def parse_in_batches(input_file, output_file, batch_size=10000, max_entries=None):
    """Parse dictionary in batches"""
    parser = OxfordDictionaryParser()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    all_entries = []
    current_word = None
    current_content = []
    
    print(f"Processing {len(lines)} lines...")
    
    for line_num, line in enumerate(lines):
        if max_entries and len(all_entries) >= max_entries:
            break
        
        stripped = line.rstrip()
        
        if line_num % 10000 == 0:
            print(f"Progress: {line_num}/{len(lines)} lines, {len(all_entries)} entries")
        
        # Check if this is a new word entry
        if parser._is_word_line(stripped):
            # Save previous entry
            if current_word and current_content:
                try:
                    entry = parser._parse_entry(current_word, '\n'.join(current_content))
                    if entry:
                        from dataclasses import asdict
                        entry_dict = asdict(entry)
                        all_entries.append(entry_dict)
                except Exception as e:
                    print(f"Error parsing entry {current_word}: {e}")
            
            # Start new entry
            match = parser._word_match(stripped)
            if match:
                current_word = match.group(1).strip()
                current_content = [stripped]
            else:
                current_word = None
                current_content = []
        else:
            if current_word:
                current_content.append(stripped)
    
    # Save last entry
    if current_word and current_content:
        try:
            entry = parser._parse_entry(current_word, '\n'.join(current_content))
            if entry:
                from dataclasses import asdict
                entry_dict = asdict(entry)
                all_entries.append(entry_dict)
        except Exception as e:
            print(f"Error parsing entry {current_word}: {e}")
    
    data = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Oxford English Dictionary",
        "total_entries": len(all_entries),
        "entries": all_entries
    }
    
    print(f"Saving {len(all_entries)} entries to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Done!")

# Monkey patch for word_match
def _word_match(self, line: str):
    return __import__('re').match(r'^([A-Za-z][A-Za-z0-9\-\s\']*)\s{2,}', line)

OxfordDictionaryParser._word_match = _word_match

if __name__ == '__main__':
    # Parse all entries
    parse_in_batches(
        '/workspace/dlake/edu/english/oxford/Oxford English Dictionary.txt',
        '/workspace/dlake/edu/english/oxford/OxfordDict.json'
    )
