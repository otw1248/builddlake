# Oxford English Dictionary Parser

This project converts the Oxford English Dictionary from plain text format to structured JSON, making it easy to search and use programmatically.

## Files Generated

- **OxfordDict.json** (39 MB) - Main dictionary with 36,090 entries
- **search_index.json** (43 MB) - Search index for fast lookups

## Dictionary Structure

Each dictionary entry follows this schema:

```json
{
  "word": "Abandon",
  "parts": [
    {
      "part_of_speech": "v.",
      "variants": [
        {
          "type": "verb",
          "definition": "Freedom from inhibitions.",
          "numbered_definitions": [
            {
              "number": "1",
              "text": "give up."
            },
            {
              "number": "2",
              "text": "forsake, desert."
            }
          ],
          "inflection": "(-ting)",
          "usage": "(often foll. By to; often refl.)",
          "pronunciation": null,
          "part_of_speech": "v."
        }
      ],
      "etymology": {
        "text": "[french: related to *ad-, *ban]",
        "language": "french",
        "related": ["ad-", "ban"],
        "from_language": null
      },
      "idioms": [],
      "derived_forms": [
        {
          "form": "abandonment",
          "partOfSpeech": "n."
        }
      ],
      "special_fields": [],
      "usage_note": null,
      "registers": [],
      "regional": null
    }
  ]
}
```

## Features

- **Word extraction**: Parses headwords from the dictionary
- **Part of speech**: Identifies nouns, verbs, adjectives, adverbs, prefixes, suffixes
- **Numbered definitions**: Handles multiple numbered definitions with sub-points
- **Etymology**: Extracts language of origin and related words
- **Idioms**: Captures idiomatic phrases
- **Derived forms**: Lists related word forms
- **Special fields**: Identifies specialized domains (nautical, architectural, etc.)
- **Usage notes**: Captures usage information
- **Regional markers**: Identifies regional variations (British, American, etc.)

## Search Capabilities

Use the `search_dict.py` utility:

```python
from search_dict import OxfordDictionarySearcher

searcher = OxfordDictionarySearcher()

# Search by exact word
result = searcher.search_by_word('abandon')

# Search by prefix
results = searcher.search_by_prefix('ab', limit=10)

# Search by definition keyword
results = searcher.search_by_definition('house', limit=5)

# Search by part of speech
results = searcher.search_by_part_of_speech('n.', limit=10)

# Search by etymology language
results = searcher.search_by_etymology_language('latin', limit=10)

# Get detailed word information
details = searcher.get_word_details('abandon')
```

## Interactive Search

Run the interactive search interface:

```bash
python search_dict.py
```

Available commands:
- `w <word>` - Search for exact word
- `p <prefix>` - Search words by prefix
- `d <keyword>` - Search by definition keyword
- `pos <tag>` - Search by part of speech
- `ety <lang>` - Search by etymology language
- `rel <word>` - Search by related words
- `info <word>` - Get detailed word information
- `q` - Quit

## Usage Examples

### Example 1: Search for a word

```python
import json

with open('OxfordDict.json', 'r') as f:
    data = json.load(f)

# Find word by iterating
for entry in data['entries']:
    if entry['word'].lower() == 'abandon':
        print(entry)
        break
```

### Example 2: Using search index

```python
import json

with open('search_index.json', 'r') as f:
    index = json.load(f)

# Fast lookup by word
word_data = index['by_word']['abandon']

# Find words by definition keyword
matching_words = index['by_definition'].get('house', [])

# Find all nouns
nouns = index['by_pos'].get('n.', [])
```

## Parser Scripts

### parse_batch.py
Parses the full dictionary file into JSON format. Handles large files efficiently.

```bash
python parse_batch.py
```

### create_search_index.py
Creates a search index for fast lookups.

```bash
python create_search_index.py
```

### oxford_parser.py
Core parser library. Can be used programmatically:

```python
from oxford_parser import OxfordDictionaryParser

parser = OxfordDictionaryParser()
data = parser.parse_file('Oxford English Dictionary.txt')
```

## Statistics

- **Total entries**: 36,090
- **Unique words**: 34,570
- **Definition keywords**: 37,685
- **Parts of speech**: prefix, suffix, v., n., adj.

## Notes

1. **Pronunciation**: The source dictionary file does not contain IPA pronunciation data. The `pronunciation` field is included in the schema for future use but will be null for most entries.

2. **Etymology**: Etymology information is extracted when present. Not all entries include etymology.

3. **Idioms**: Idioms are detected using pattern matching. Some idiomatic phrases may not be captured.

4. **Variants**: Multi-part-of-speech entries are split into separate parts.

## Schema Reference

See `schema.txt` for the complete JSON schema specification.

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## License

This parser is provided as-is for educational and research purposes. The Oxford English Dictionary source text is copyrighted material.
