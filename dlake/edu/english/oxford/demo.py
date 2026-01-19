# Created by AI Assistant on 2026-01-19
"""
Demonstration of Oxford Dictionary JSON usage
"""

import json

def demo():
    print("=" * 60)
    print("Oxford English Dictionary - JSON Demo")
    print("=" * 60)
    print()

    # Load dictionary
    print("Loading dictionary...")
    with open('OxfordDict.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"Total entries: {data['total_entries']}")
    print()

    # Example 1: Direct word lookup
    print("-" * 60)
    print("Example 1: Word Lookup")
    print("-" * 60)

    # Find 'abandon'
    for entry in data['entries']:
        if entry['word'].lower() == 'abandon':
            print(f"\nWord: {entry['word']}")
            for part in entry['parts']:
                if part.get('etymology'):
                    etym = part['etymology']
                    print(f"Etymology: {etym['text']} ({etym.get('language', 'unknown')})")
                for variant in part.get('variants', []):
                    if variant.get('numbered_definitions'):
                        print("Definitions:")
                        for d in variant.get('numbered_definitions'):
                            print(f"  {d['number']}. {d['text']}")
                    if variant.get('definition'):
                        print(f"Definition: {variant['definition']}")
                    if variant.get('derived_forms'):
                        print("Derived forms:", ', '.join([df['form'] for df in part.get('derived_forms', [])]))
            break

    # Example 2: Using search index
    print("\n" + "-" * 60)
    print("Example 2: Using Search Index")
    print("-" * 60)

    with open('search_index.json', 'r', encoding='utf-8') as f:
        index = json.load(f)

    # Fast word lookup
    print(f"\nWords starting with 'ab':")
    for word in sorted(index['by_word'].keys()):
        if word.startswith('ab'):
            print(f"  - {word}")
            if len([w for w in index['by_word'].keys() if w.startswith('ab')]) > 10:
                print(f"  ... and more")
                break

    # Find words by definition
    print(f"\nWords with 'house' in definition:")
    house_words = index['by_definition'].get('house', [])
    print(f"  Found {len(house_words)} words")
    for w in house_words[:5]:
        print(f"  - {w}")

    # Find all nouns
    print(f"\nNouns in dictionary:")
    nouns = index['by_pos'].get('n.', [])
    print(f"  Found {len(nouns)} nouns")
    print(f"  First 10: {nouns[:10]}")

    # Example 3: Search for specific patterns
    print("\n" + "-" * 60)
    print("Example 3: Advanced Search")
    print("-" * 60)

    # Find words with 'latin' etymology
    print("\nWords with Latin etymology:")
    count = 0
    for entry in data['entries'][:100]:  # Check first 100 for demo
        for part in entry['parts']:
            if part.get('etymology'):
                lang = part['etymology'].get('language') or ''
                if 'latin' in lang.lower():
                    print(f"  - {entry['word']} ({lang})")
                    count += 1
                    if count >= 5:
                        break
        if count >= 5:
            break

    # Find multi-definition words
    print("\nWords with multiple numbered definitions:")
    count = 0
    for entry in data['entries']:
        for part in entry['parts']:
            for variant in part.get('variants', []):
                num_defs = len(variant.get('numbered_definitions', []))
                if num_defs >= 3:
                    print(f"  - {entry['word']}: {num_defs} definitions")
                    count += 1
                    if count >= 5:
                        break
        if count >= 5:
            break

    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)

if __name__ == '__main__':
    demo()
