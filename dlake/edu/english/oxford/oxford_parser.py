# Created by AI Assistant on 2026-01-19
"""
Oxford Dictionary Parser
Converts Oxford English Dictionary text format to structured JSON
"""

import re
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict, field


@dataclass
class Etymology:
    text: str
    language: Optional[str] = None
    related: List[str] = field(default_factory=list)
    from_language: Optional[str] = None


@dataclass
class Variant:
    type: Optional[str] = None
    definition: Optional[str] = None
    numbered_definitions: List[Dict[str, str]] = field(default_factory=list)
    inflection: Optional[str] = None
    usage: Optional[str] = None
    pronunciation: Optional[str] = None
    part_of_speech: Optional[str] = None


@dataclass
class DictionaryPart:
    part_of_speech: Optional[str] = None
    variants: List[Variant] = field(default_factory=list)
    etymology: Optional[Etymology] = None
    cross_references: List[str] = field(default_factory=list)
    idioms: List[Dict[str, str]] = field(default_factory=list)
    examples: List[str] = field(default_factory=list)
    phrases: List[Dict[str, str]] = field(default_factory=list)
    special_fields: List[str] = field(default_factory=list)
    derived_forms: List[Dict[str, str]] = field(default_factory=list)
    usage_note: Optional[str] = None
    registers: List[str] = field(default_factory=list)
    regional: Optional[str] = None


@dataclass
class DictionaryEntry:
    word: str
    parts: List[DictionaryPart] = field(default_factory=list)


class OxfordDictionaryParser:
    """Parser for Oxford English Dictionary text format"""
    
    def __init__(self):
        # Part of speech patterns
        self.pos_patterns = [
            ('n\\.', 'noun'),
            ('v\\.', 'verb'),
            ('adj\\.', 'adjective'),
            ('adv\\.', 'adverb'),
            ('prefix', 'prefix'),
            ('suffix', 'suffix'),
            ('abbr\\.', 'abbreviation'),
            ('int\\.', 'interjection'),
            ('—n\\.', 'noun'),
            ('—adj\\.', 'adjective'),
            ('—v\\.', 'verb'),
            ('—adv\\.', 'adverb'),
            ('—int\\.', 'interjection'),
            ('predic\\. adj\\.', 'adjective'),
        ]
        
        # Specialized fields
        self.special_fields = [
            'naut.', 'archit.', 'gram.', 'biol.', 'astron.', 
            'chem.', 'phys.', 'mus.', 'phil.', 'psych.', 
            'hist.', 'med.', 'zool.', 'bot.', 'geol.',
            'math.', 'law', 'eccles.', 'optics', 'phonet.'
        ]
        
        # Register markers
        self.registers = ['colloq.', 'archaic', 'slang', 'offens.', 'rare', 'obs.', 'usu.']
        
        # Regional markers
        self.regionals = ['austral.', 'brit.', 'us', 'scot.', 'amer.', 'ind.', 'canad.', 'irish.']
    
    def parse_file(self, filepath: str) -> Dict[str, Any]:
        """Parse the entire dictionary file and return structured data"""
        entries = []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Parse entries line by line
        current_word = None
        current_content = []
        
        for line_num, line in enumerate(lines):
            stripped = line.rstrip()
            
            # Check if this is a new word entry (starts with capital letter(s) followed by tabs)
            if self._is_word_line(stripped):
                # Save previous entry
                if current_word and current_content:
                    entry = self._parse_entry(current_word, '\n'.join(current_content))
                    if entry:
                        entries.append(asdict(entry))
                
                # Start new entry
                match = re.match(r'^([A-Za-z][A-Za-z0-9\-\s\']*)\s{2,}', stripped)
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
            entry = self._parse_entry(current_word, '\n'.join(current_content))
            if entry:
                entries.append(asdict(entry))
        
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "Oxford English Dictionary",
            "total_entries": len(entries),
            "entries": entries
        }
    
    def _is_word_line(self, line: str) -> bool:
        """Check if a line starts with a new word entry"""
        # Pattern: starts with capital letter(s), followed by 2+ spaces/tabs
        # Skip lines that are too short or start with lowercase
        if len(line) < 3:
            return False
        if line[0].islower():
            return False
        
        # Check for word pattern (capital letter + possibly more letters/hyphens, then 2+ spaces)
        match = re.match(r'^[A-Z][A-Za-z0-9\-\s\']*\s{2,}', line)
        return bool(match)
    
    def _parse_entry(self, word: str, content: str) -> Optional[DictionaryEntry]:
        """Parse a single dictionary entry"""
        entry = DictionaryEntry(word=word)
        
        # Split content into parts (multiple POS or usages)
        parts = self._split_into_parts(content)
        
        for part_content in parts:
            part = self._parse_part(part_content)
            if part:
                entry.parts.append(part)
        
        return entry if entry.parts else None
    
    def _split_into_parts(self, content: str) -> List[str]:
        """Split content into multiple parts based on POS markers"""
        parts = []
        current_part = []
        lines = content.split('\n')
        
        for line in lines:
            # Check if line starts with a new POS marker
            has_new_pos = False
            for pos_pattern, _ in self.pos_patterns:
                if re.match(r'^—?\s*' + pos_pattern, line.strip()) or \
                   re.match(r'^' + pos_pattern, line.strip()):
                    has_new_pos = True
                    break
            
            if has_new_pos and current_part:
                parts.append('\n'.join(current_part))
                current_part = [line]
            else:
                current_part.append(line)
        
        if current_part:
            parts.append('\n'.join(current_part))
        
        return parts
    
    def _parse_part(self, content: str) -> Optional[DictionaryPart]:
        """Parse a part of the dictionary entry"""
        part = DictionaryPart()
        full_content = content
        
        # Extract etymology (last bracket pattern)
        etymology = self._extract_etymology(full_content)
        if etymology:
            part.etymology = etymology
            # Remove etymology from content
            full_content = re.sub(r'\s*\[[^\]]+\]\s*$', '', full_content)
        
        # Extract part of speech
        pos_tag, pos_type = self._extract_part_of_speech(full_content)
        part.part_of_speech = pos_tag
        
        # Extract special fields
        special_fields = self._extract_special_fields(full_content)
        if special_fields:
            part.special_fields = special_fields
            # Remove special fields from content
            for sf in special_fields:
                full_content = re.sub(r'\b' + re.escape(sf) + r'\b\s*', '', full_content, count=1)
        
        # Extract regional markers
        regional = self._extract_regional(full_content)
        if regional:
            part.regional = regional
            full_content = re.sub(r'\b' + re.escape(regional) + r'\b\s*', '', full_content, count=1)
        
        # Extract registers
        registers = self._extract_registers(full_content)
        if registers:
            part.registers = registers
            for reg in registers:
                full_content = re.sub(r'\b' + re.escape(reg) + r'\b\s*', '', full_content, count=1)
        
        # Extract idioms
        idioms = self._extract_idioms(full_content)
        if idioms:
            part.idioms = idioms
        
        # Extract derived forms (after bullet character)
        derived = self._extract_derived_forms(full_content)
        if derived:
            part.derived_forms = derived
        
        # Extract cross-references
        cross_refs = self._extract_cross_references(full_content)
        if cross_refs:
            part.cross_references = cross_refs
        
        # Extract usage note
        usage = self._extract_usage_note(full_content)
        if usage:
            part.usage_note = usage
        
        # Parse variants/definitions
        variants = self._parse_variants(full_content, pos_tag)
        if variants:
            part.variants = variants
        
        return part
    
    def _extract_part_of_speech(self, content: str) -> tuple:
        """Extract part of speech tag and type"""
        for pattern, pos_type in self.pos_patterns:
            match = re.search(r'\b' + pattern + r'\b', content)
            if match:
                return match.group(), pos_type
        return None, None
    
    def _extract_etymology(self, content: str) -> Optional[Etymology]:
        """Extract etymology from brackets"""
        matches = re.findall(r'\[([^\]]+)\]', content)
        if matches:
            # Take the last match (usually the etymology)
            text = matches[-1]
            etymology = Etymology(text=f"[{text}]")
            
            # Extract language
            languages = ['latin', 'greek', 'french', 'old english', 'german', 
                        'spanish', 'italian', 'hebrew', 'arabic', 'afrikaans',
                        'medieval latin', 'anglo-latin', 'sanskrit', 'scottish']
            for lang in languages:
                if lang in text.lower():
                    etymology.language = lang
                    break
            
            # Extract related words (marked with asterisk)
            related = re.findall(r'\*([a-zA-Z0-9\-]+)', text)
            if related:
                etymology.related = related
            
            # Extract from language
            from_match = re.search(r'from\s+([a-zA-Z\s]+)', text)
            if from_match:
                etymology.from_language = from_match.group(1).strip()
            
            return etymology
        return None
    
    def _extract_special_fields(self, content: str) -> List[str]:
        """Extract specialized field indicators"""
        found = []
        for sf in self.special_fields:
            if re.search(r'\b' + re.escape(sf) + r'\b', content):
                found.append(sf)
        return found
    
    def _extract_regional(self, content: str) -> Optional[str]:
        """Extract regional marker"""
        for reg in self.regionals:
            if re.search(r'\b' + re.escape(reg) + r'\b', content):
                return reg
        return None
    
    def _extract_registers(self, content: str) -> List[str]:
        """Extract register markers"""
        found = []
        for reg in self.registers:
            if re.search(r'\b' + re.escape(reg) + r'\b', content):
                found.append(reg)
        return found
    
    def _extract_idioms(self, content: str) -> List[Dict[str, str]]:
        """Extract idiomatic phrases"""
        idioms = []
        # Look for common idiom patterns
        # Pattern: word followed by definition that suggests a phrase
        idiom_patterns = [
            r'(take [a-z]+)\s+([^.]+[.])',
            r'(be [a-z]+)\s+([^.]+[.])',
            r'(have [a-z]+)\s+([^.]+[.])',
            r'(get [a-z]+)\s+([^.]+[.])',
            r'(put [a-z]+)\s+([^.]+[.])',
            r'(keep [a-z]+)\s+([^.]+[.])',
        ]
        
        for pattern in idiom_patterns:
            matches = re.findall(pattern, content)
            for phrase, definition in matches:
                if len(phrase) > 3 and len(definition) > 5:
                    idioms.append({
                        "phrase": phrase.strip(),
                        "definition": definition.strip()
                    })
        
        return idioms
    
    def _extract_derived_forms(self, content: str) -> List[Dict[str, str]]:
        """Extract derived forms"""
        derived = []
        # Pattern: bullet character followed by word and POS
        # Note: The bullet character is a special char that needs to be handled
        bullet_content = content.split('\x7f')  # Unicode DEL often used as bullet
        for item in bullet_content[1:]:  # Skip first (main word)
            item = item.strip()
            # Look for word followed by n., adj., etc.
            match = re.match(r'([a-zA-Z\-]+)\s+(n\.|adj\.|adv\.|v\.)', item)
            if match:
                word, pos = match.groups()
                derived.append({
                    "form": word,
                    "partOfSpeech": pos
                })
        
        return derived
    
    def _extract_cross_references(self, content: str) -> List[str]:
        """Extract cross-references"""
        refs = []
        patterns = [
            r'see\s+\*?([a-zA-Z0-9\-]+)',
            r'=\s+\*?([a-zA-Z0-9\-]+)',
        ]
        for pattern in patterns:
            matches = re.findall(pattern, content)
            refs.extend(matches)
        return list(set(refs))
    
    def _extract_usage_note(self, content: str) -> Optional[str]:
        """Extract usage notes"""
        if 'Usage' in content:
            match = re.search(r'Usage\s+([^.]+)', content)
            if match:
                return match.group(1).strip()
        return None
    
    def _parse_variants(self, content: str, pos_tag: Optional[str]) -> List[Variant]:
        """Parse variants and definitions"""
        variants = []
        
        # Split by POS markers (—n., —v., —adj., —adv., —int.)
        variant_blocks = self._split_by_pos_markers(content)
        
        for block in variant_blocks:
            variant = Variant()
            
            # Determine POS for this variant
            block_pos_tag, block_pos_type = self._extract_part_of_speech(block)
            variant.part_of_speech = block_pos_tag
            variant.type = block_pos_type
            
            # Extract inflection
            inflection = self._extract_inflection(block)
            if inflection:
                variant.inflection = inflection
            
            # Extract usage pattern
            usage = self._extract_usage_pattern(block)
            if usage:
                variant.usage = usage
            
            # Check for numbered definitions
            numbered_defs = self._extract_numbered_definitions(block)
            if numbered_defs:
                variant.numbered_definitions = numbered_defs
            else:
                # Simple definition
                definition = self._clean_definition(block)
                if definition:
                    variant.definition = definition
            
            if variant.definition or variant.numbered_definitions:
                variants.append(variant)
        
        return variants
    
    def _split_by_pos_markers(self, content: str) -> List[str]:
        """Split content by POS markers"""
        markers = ['—n.', '—v.', '—adj.', '—adv.', '—int.', '—prep.', '—pron.']
        parts = [content]
        
        for marker in markers:
            new_parts = []
            for part in parts:
                if marker in part:
                    subparts = part.split(marker, 1)
                    new_parts.extend(subparts)
                else:
                    new_parts.append(part)
            parts = new_parts
        
        return parts
    
    def _extract_inflection(self, content: str) -> Optional[str]:
        """Extract inflection patterns"""
        patterns = [
            r'\(-[a-z]+\)',  # (-ting), (-sing)
            r'\(-[a-z]+\s+or\s+rarely\s+[a-z-]+\)',  # (past abided or rarely abode)
            r'\(pl\.\s+[-a-z]+\)',  # (pl. -cuses)
            r'\(pl\.\s+[-a-z]+,\s+[-a-z]+\)',  # (pl. -ies, pl. -s)
        ]
        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(0)
        return None
    
    def _extract_usage_pattern(self, content: str) -> Optional[str]:
        """Extract usage patterns"""
        patterns = [
            r'\(often\s+foll\.\s+by\s+[a-z]+\)',
            r'\(usu\.\s+foll\.\s+by\s+[a-z]+\)',
            r'\(also\s+refl\.\)',
            r'\(rarely\s+[a-z]+\)',
            r'\(usu\.\)',
            r'\(often\s+absol\.\)',
            r'\(in\s+neg\.\)',
            r'\(also\s+absol\.\)',
        ]
        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(0)
        return None
    
    def _extract_numbered_definitions(self, content: str) -> List[Dict[str, str]]:
        """Extract numbered definitions"""
        defs = []
        
        # Remove content before first number
        first_num = re.search(r'\b\d+\s', content)
        if first_num:
            content = content[first_num.start():]
        
        # Find all numbered definitions
        # Pattern: 1 text 2 text 3 text etc.
        parts = re.split(r'(\d+)\s+', content)
        
        current_num = None
        current_text = []
        
        for i, part in enumerate(parts):
            if re.match(r'^\d+$', part):
                # Save previous definition
                if current_num and current_text:
                    text = ' '.join(current_text).strip()
                    if text:
                        defs.append({
                            "number": current_num,
                            "text": text
                        })
                current_num = part
                current_text = []
            else:
                if current_num:
                    # Filter out unwanted content
                    skip_patterns = [
                        r'^—',
                        r'^n\.', r'^v\.', r'^adj\.', r'^adv\.',
                        r'^\[', r'^Usage',
                        r'^'
                    ]
                    if not any(re.match(p, part.strip()) for p in skip_patterns):
                        current_text.append(part)
        
        # Add last definition
        if current_num and current_text:
            text = ' '.join(current_text).strip()
            if text:
                defs.append({
                    "number": current_num,
                    "text": text
                })
        
        return defs
    
    def _clean_definition(self, content: str) -> Optional[str]:
        """Clean and extract simple definition"""
        # Remove common markers
        clean = content
        
        # Remove POS tags
        for pattern, _ in self.pos_patterns:
            clean = re.sub(r'\b' + pattern + r'\b', '', clean)
        
        # Remove special fields
        for sf in self.special_fields:
            clean = re.sub(r'\b' + re.escape(sf) + r'\b', '', clean)
        
        # Remove etymology brackets
        clean = re.sub(r'\[[^\]]*\]', '', clean)
        
        # Remove usage patterns
        clean = re.sub(r'\([^)]*\)', '', clean)
        
        # Remove register markers
        for reg in self.registers:
            clean = re.sub(r'\b' + re.escape(reg) + r'\b', '', clean)
        
        # Remove special characters
        clean = re.sub(r'^—\s*', '', clean)
        clean = clean.replace('\x7f', '').strip()
        
        # Clean up whitespace
        clean = re.sub(r'\s+', ' ', clean).strip()
        
        return clean if len(clean) > 2 else None


def create_search_index(entries: List[Dict]) -> Dict[str, Any]:
    """Create a search index for easy lookup"""
    index = {
        "by_word": {},
        "by_definition": {},
        "total_words": len(entries)
    }
    
    for entry in entries:
        word = entry.get('word', '').lower()
        index["by_word"][word] = entry
        
        # Index by definition words
        for part in entry.get('parts', []):
            for variant in part.get('variants', []):
                def_text = variant.get('definition', '')
                for num_def in variant.get('numbered_definitions', []):
                    def_text += ' ' + num_def.get('text', '')
                
                # Extract meaningful words from definition
                words = re.findall(r'\b[a-z]{3,}\b', def_text.lower())
                for w in words[:10]:
                    if w not in index["by_definition"]:
                        index["by_definition"][w] = []
                    if word not in index["by_definition"][w]:
                        index["by_definition"][w].append(word)
    
    return index


def main():
    """Main function to parse dictionary"""
    parser = OxfordDictionaryParser()
    
    input_file = '/workspace/dlake/edu/english/oxford/Oxford English Dictionary.txt'
    output_file = '/workspace/dlake/edu/english/oxford/OxfordDict.json'
    index_file = '/workspace/dlake/edu/english/oxford/search_index.json'
    
    print(f"Parsing dictionary from: {input_file}")
    data = parser.parse_file(input_file)
    
    print(f"Found {data['total_entries']} entries")
    
    # Save main dictionary
    print(f"Saving to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Create and save search index
    print("Creating search index...")
    index = create_search_index(data['entries'])
    
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    print(f"Search index saved to: {index_file}")
    print(f"Done!")


if __name__ == '__main__':
    main()
