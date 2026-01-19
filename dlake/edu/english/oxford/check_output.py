# Created by AI Assistant on 2026-01-19
"""Check generated files"""

import json

# Load and check dictionary
with open('OxfordDict.json', 'r') as f:
    data = json.load(f)

print('Dictionary Info:')
print(f'  Total entries: {data["total_entries"]}')
print(f'  Schema: {data["$schema"]}')
print()

# Show first entry structure
first = data['entries'][0]
print('First entry:', first['word'])
print('Number of parts:', len(first['parts']))
print()

# Show index
with open('search_index.json', 'r') as f:
    index = json.load(f)

print('Search Index Info:')
print(f'  Total words: {index["total_words"]}')
print(f'  Unique words: {len(index["by_word"])}')
print(f'  Definition keywords: {len(index["by_definition"])}')
print(f'  Parts of speech: {list(index["by_pos"].keys())}')
