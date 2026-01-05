#!/usr/bin/env python3
import json
import re
from collections import Counter

def clean_and_split_text(text):
    """Clean text and split into words, excluding signs and empty strings"""
    # Remove punctuation and special characters, keep only letters and spaces
    cleaned = re.sub(r'[^\w\s\']', ' ', text)
    # Split by whitespace
    words = cleaned.split()
    # Filter: length > 2 and not empty
    words = [word.lower() for word in words if len(word) > 2 and word.strip()]
    return words

def main():
    # Read both JSON files
    print("Reading JSON files...")
    
    with open('/workspace/dlake/edu/english/pschool/unit-data.json', 'r', encoding='utf-8') as f:
        unit_data = json.load(f)
    
    with open('/workspace/dlake/edu/english/pschool/english-units.json', 'r', encoding='utf-8') as f:
        english_units = json.load(f)
    
    print(f"Loaded unit-data.json with {len(unit_data.get('words', []))} words, "
          f"{len(unit_data.get('phrases', []))} phrases, "
          f"{len(unit_data.get('sentences', []))} sentences")
    
    # Collect all words
    all_words = []
    
    # Process words
    for item in unit_data.get('words', []):
        if 'word' in item:
            all_words.extend(clean_and_split_text(item['word']))
    
    # Process phrases
    for item in unit_data.get('phrases', []):
        if 'phrase' in item:
            all_words.extend(clean_and_split_text(item['phrase']))
    
    # Process sentences
    for item in unit_data.get('sentences', []):
        if 'sentence' in item:
            all_words.extend(clean_and_split_text(item['sentence']))
    
    print(f"\nTotal words collected: {len(all_words)}")
    print(f"Unique words: {len(set(all_words))}")
    
    # Count word frequencies
    word_counter = Counter(all_words)
    
    # Sort by count (descending) and get top 100
    top_100 = word_counter.most_common(100)
    
    print("\n" + "="*60)
    print("TOP 100 MOST COMMON WORDS (length > 2)")
    print("="*60)
    print(f"{'Rank':<8}{'Word':<25}{'Count':<10}")
    print("-"*60)
    
    for rank, (word, count) in enumerate(top_100, 1):
        print(f"{rank:<8}{word:<25}{count:<10}")
    
    # Save to JSON file
    result = {
        'total_words': len(all_words),
        'unique_words': len(set(all_words)),
        'top_100_words': [
            {'rank': i+1, 'word': word, 'count': count}
            for i, (word, count) in enumerate(top_100)
        ]
    }
    
    with open('/workspace/word_analysis_result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*60)
    print("Results saved to: /workspace/word_analysis_result.json")

if __name__ == '__main__':
    main()
