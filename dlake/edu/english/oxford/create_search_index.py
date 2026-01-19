# Created by AI Assistant on 2026-01-19
"""
Create search index for Oxford Dictionary JSON
"""

import json
import re

def create_search_index(dict_file: str, index_file: str):
    """Create a search index for easy lookup"""
    
    print(f"Loading dictionary from {dict_file}...")
    with open(dict_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    entries = data['entries']
    
    index = {
        "by_word": {},
        "by_definition": {},
        "by_pos": {},
        "total_words": len(entries)
    }
    
    print(f"Indexing {len(entries)} entries...")
    
    for i, entry in enumerate(entries):
        if i % 5000 == 0:
            print(f"Progress: {i}/{len(entries)}")
        
        word = entry.get('word', '').lower()
        index["by_word"][word] = entry
        
        # Index by part of speech
        for part in entry.get('parts', []):
            pos = part.get('part_of_speech')
            if pos:
                if pos not in index["by_pos"]:
                    index["by_pos"][pos] = []
                if word not in index["by_pos"][pos]:
                    index["by_pos"][pos].append(word)
            
            # Index by definition words
            for variant in part.get('variants', []):
                def_text = variant.get('definition', '') or ''
                for num_def in variant.get('numbered_definitions', []):
                    if num_def and isinstance(num_def, dict):
                        def_text += ' ' + (num_def.get('text', '') or '')
                
                # Extract meaningful words from definition
                words = re.findall(r'\b[a-z]{3,}\b', def_text.lower())
                for w in words[:10]:
                    if w not in index["by_definition"]:
                        index["by_definition"][w] = []
                    if word not in index["by_definition"][w]:
                        index["by_definition"][w].append(word)
    
    print(f"Saving index to {index_file}...")
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    print(f"Index statistics:")
    print(f"  Total words: {len(index['by_word'])}")
    print(f"  Definition keywords: {len(index['by_definition'])}")
    print(f"  Parts of speech: {list(index['by_pos'].keys())}")
    print(f"Done!")

if __name__ == '__main__':
    create_search_index(
        '/workspace/dlake/edu/english/oxford/OxfordDict.json',
        '/workspace/dlake/edu/english/oxford/search_index.json'
    )
