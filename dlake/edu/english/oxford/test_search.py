# Created by AI Assistant on 2026-01-19
"""Test search functionality"""

from search_dict import OxfordDictionarySearcher

searcher = OxfordDictionarySearcher()

# Test search by word
print('=== Search by word: abandon ===')
result = searcher.search_by_word('abandon')
if result:
    print(f'Found: {result["word"]}')
    for part in result['parts']:
        print(f'  POS: {part.get("part_of_speech")}')
        for variant in part.get('variants', []):
            if variant.get('definition'):
                print(f'  Definition: {variant["definition"][:80]}...')
            for num_def in variant.get('numbered_definitions', []):
                print(f'  {num_def["number"]}. {num_def["text"][:60]}...')

print()
print('=== Search by prefix: ab ===')
results = searcher.search_by_prefix('ab', limit=5)
for r in results:
    print(f'  - {r["word"]}')

print()
print('=== Search by definition: house ===')
results = searcher.search_by_definition('house', limit=3)
for r in results:
    print(f'  - {r["word"]}')

print()
print('=== Search by POS: n. ===')
results = searcher.search_by_part_of_speech('n.', limit=3)
for r in results:
    print(f'  - {r["word"]}')
