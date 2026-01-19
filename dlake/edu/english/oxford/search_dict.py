# Created by AI Assistant on 2026-01-19
"""
Oxford Dictionary Search Utility
Provides easy search functionality for the Oxford Dictionary JSON
"""

import json
from typing import List, Dict, Any


class OxfordDictionarySearcher:
    """Search utility for Oxford Dictionary JSON"""
    
    def __init__(self, dict_file: str = 'OxfordDict.json', 
                 index_file: str = 'search_index.json'):
        self.dict_file = dict_file
        self.index_file = index_file
        self.entries = []
        self.word_index = {}
        self.definition_index = {}
        
        self._load_data()
    
    def _load_data(self):
        """Load dictionary data from JSON files"""
        print(f"Loading dictionary from {self.dict_file}...")
        with open(self.dict_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.entries = data.get('entries', [])
        
        # Build word index if not loading from index file
        print("Building word index...")
        for entry in self.entries:
            word = entry.get('word', '').lower()
            self.word_index[word] = entry
        
        print(f"Loaded {len(self.entries)} entries")
    
    def search_by_word(self, word: str) -> Dict[str, Any]:
        """Search for an exact word match"""
        word_lower = word.lower().strip()
        return self.word_index.get(word_lower)
    
    def search_by_prefix(self, prefix: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Search for words starting with a prefix"""
        prefix_lower = prefix.lower().strip()
        results = []
        
        for word in sorted(self.word_index.keys()):
            if word.startswith(prefix_lower):
                results.append(self.word_index[word])
                if len(results) >= limit:
                    break
        
        return results
    
    def search_by_definition(self, keyword: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Search for entries by definition keywords"""
        keyword_lower = keyword.lower().strip()
        results = []
        seen = set()
        
        for entry in self.entries:
            word = entry.get('word', '').lower()
            if word in seen:
                continue
            
            # Check all definitions in the entry
            for part in entry.get('parts', []):
                for variant in part.get('variants', []):
                    # Check main definition
                    definition = variant.get('definition')
                    if definition and keyword_lower in definition.lower():
                        results.append(entry)
                        seen.add(word)
                        break
                    
                    # Check numbered definitions
                    for num_def in variant.get('numbered_definitions', []):
                        def_text = num_def.get('text', '') if isinstance(num_def, dict) else ''
                        if def_text and keyword_lower in def_text.lower():
                            results.append(entry)
                            seen.add(word)
                            break
                
                # Check idioms
                for idiom in part.get('idioms', []):
                    if keyword_lower in idiom.get('definition', '').lower():
                        results.append(entry)
                        seen.add(word)
                        break
                
                if word in seen:
                    break
            
            if len(results) >= limit:
                break
        
        return results
    
    def search_by_part_of_speech(self, pos: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Search for entries by part of speech"""
        results = []
        
        for entry in self.entries:
            for part in entry.get('parts', []):
                part_pos = part.get('part_of_speech')
                if part_pos and pos.lower() in part_pos.lower():
                    results.append(entry)
                    break
            
            if len(results) >= limit:
                break
        
        return results
    
    def search_by_etymology_language(self, language: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Search for entries by etymology language"""
        results = []
        language_lower = language.lower()
        
        for entry in self.entries:
            for part in entry.get('parts', []):
                etymology = part.get('etymology', {})
                if etymology and language_lower in etymology.get('language', '').lower():
                    results.append(entry)
                    break
            
            if len(results) >= limit:
                break
        
        return results
    
    def search_by_related_words(self, related_word: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Search for entries with related words in etymology"""
        results = []
        related_lower = related_word.lower()
        
        for entry in self.entries:
            for part in entry.get('parts', []):
                etymology = part.get('etymology', {})
                if etymology:
                    related = etymology.get('related', [])
                    if related_lower in [r.lower() for r in related]:
                        results.append(entry)
                        break
            
            if len(results) >= limit:
                break
        
        return results
    
    def get_word_details(self, word: str) -> Dict[str, Any]:
        """Get detailed information about a word"""
        entry = self.search_by_word(word)
        
        if not entry:
            return {"error": f"Word '{word}' not found"}
        
        details = {
            "word": entry.get('word'),
            "parts_of_speech": [],
            "etymology": None,
            "idioms": [],
            "phrases": [],
            "derived_forms": [],
            "examples": []
        }
        
        for part in entry.get('parts', []):
            if part.get('part_of_speech'):
                details['parts_of_speech'].append(part.get('part_of_speech'))
            
            if part.get('etymology') and not details['etymology']:
                details['etymology'] = part.get('etymology')
            
            details['idioms'].extend(part.get('idioms', []))
            details['phrases'].extend(part.get('phrases', []))
            details['derived_forms'].extend(part.get('derived_forms', []))
            details['examples'].extend(part.get('examples', []))
        
        return details
    
    def format_entry(self, entry: Dict[str, Any]) -> str:
        """Format an entry for display"""
        lines = []
        lines.append(f"Word: {entry.get('word')}")
        lines.append("-" * 50)
        
        for part in entry.get('parts', []):
            if part.get('part_of_speech'):
                lines.append(f"\nPart of Speech: {part.get('part_of_speech')}")
            
            if part.get('special_fields'):
                lines.append(f"Fields: {', '.join(part.get('special_fields', []))}")
            
            if part.get('registers'):
                lines.append(f"Register: {', '.join(part.get('registers', []))}")
            
            if part.get('regional'):
                lines.append(f"Regional: {part.get('regional')}")
            
            for variant in part.get('variants', []):
                if variant.get('definition'):
                    lines.append(f"Definition: {variant.get('definition')}")
                
                if variant.get('numbered_definitions'):
                    lines.append("Definitions:")
                    for num_def in variant.get('numbered_definitions'):
                        lines.append(f"  {num_def.get('number')}. {num_def.get('text')}")
            
            if part.get('etymology'):
                etym = part.get('etymology')
                lines.append(f"\nEtymology: {etym.get('text')}")
                if etym.get('language'):
                    lines.append(f"  Language: {etym.get('language')}")
                if etym.get('related'):
                    lines.append(f"  Related: {', '.join(etym.get('related'))}")
            
            if part.get('idioms'):
                lines.append("\nIdioms:")
                for idiom in part.get('idioms'):
                    lines.append(f"  {idiom.get('phrase')}: {idiom.get('definition')}")
            
            if part.get('derived_forms'):
                lines.append("\nDerived Forms:")
                for df in part.get('derived_forms'):
                    lines.append(f"  {df.get('form')} ({df.get('partOfSpeech')})")
            
            if part.get('usage_note'):
                lines.append(f"\nUsage: {part.get('usage_note')}")
        
        return '\n'.join(lines)


def interactive_search():
    """Interactive search interface"""
    searcher = OxfordDictionarySearcher()
    
    print("\n" + "="*60)
    print("Oxford Dictionary Search")
    print("="*60)
    print("\nCommands:")
    print("  w <word>     - Search for exact word")
    print("  p <prefix>   - Search words by prefix")
    print("  d <keyword>  - Search by definition keyword")
    print("  pos <tag>    - Search by part of speech")
    print("  ety <lang>   - Search by etymology language")
    print("  rel <word>   - Search by related words")
    print("  info <word>  - Get detailed word information")
    print("  q            - Quit")
    print("="*60 + "\n")
    
    while True:
        try:
            cmd = input("search> ").strip()
            
            if not cmd:
                continue
            
            if cmd.lower() == 'q':
                print("Goodbye!")
                break
            
            parts = cmd.split(maxsplit=1)
            command = parts[0].lower()
            query = parts[1] if len(parts) > 1 else ''
            
            if command == 'w' and query:
                result = searcher.search_by_word(query)
                if result:
                    print("\n" + searcher.format_entry(result) + "\n")
                else:
                    print(f"Word '{query}' not found\n")
            
            elif command == 'p' and query:
                results = searcher.search_by_prefix(query)
                print(f"\nFound {len(results)} words starting with '{query}':")
                for r in results:
                    print(f"  - {r.get('word')}")
                print()
            
            elif command == 'd' and query:
                results = searcher.search_by_definition(query)
                print(f"\nFound {len(results)} entries with '{query}' in definition:")
                for r in results:
                    print(f"  - {r.get('word')}")
                print()
            
            elif command == 'pos' and query:
                results = searcher.search_by_part_of_speech(query)
                print(f"\nFound {len(results)} {query} entries:")
                for r in results[:10]:
                    print(f"  - {r.get('word')}")
                print()
            
            elif command == 'ety' and query:
                results = searcher.search_by_etymology_language(query)
                print(f"\nFound {len(results)} entries from {query}:")
                for r in results[:10]:
                    print(f"  - {r.get('word')}")
                print()
            
            elif command == 'rel' and query:
                results = searcher.search_by_related_words(query)
                print(f"\nFound {len(results)} entries related to '{query}':")
                for r in results[:10]:
                    print(f"  - {r.get('word')}")
                print()
            
            elif command == 'info' and query:
                details = searcher.get_word_details(query)
                if 'error' not in details:
                    print(f"\nWord: {details['word']}")
                    print(f"Parts of Speech: {', '.join(details['parts_of_speech'])}")
                    if details['etymology']:
                        print(f"Etymology: {details['etymology']['text']}")
                    if details['idioms']:
                        print(f"Idioms: {len(details['idioms'])}")
                    if details['phrases']:
                        print(f"Phrases: {len(details['phrases'])}")
                    if details['derived_forms']:
                        print(f"Derived Forms: {', '.join([df['form'] for df in details['derived_forms']])}")
                    print()
                else:
                    print(f"\n{details['error']}\n")
            
            else:
                print(f"Unknown command: {cmd}")
                print("Type 'w', 'p', 'd', 'pos', 'ety', 'rel', 'info', or 'q'\n")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == '__main__':
    interactive_search()
