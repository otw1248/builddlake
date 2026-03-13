#!/usr/bin/env python3
"""
Created by AI Assistant
Date: 2026-03-12

Extract hierarchical terms from PDF and save to JSON format.
Handles 3-line term ID pattern and pseudo-English characters.
"""

import re
import json
import subprocess


# Mapping of pseudo-English characters to actual Latin letters
PSEUDO_ENGLISH_MAP = {
    '犪': 'a', '犫': 'b', '犮': 'c', '犱': 'd', '犲': 'e', '犳': 'f', '犳': 'f', '犵': 'g',
    '犺': 'h', '犻': 'i', '犼': 'j', '犽': 'k', '犾': 'l', '犿': 'm', '狀': 'n', '狅': 'o',
    '狆': 'p', '狇': 'q', '狉': 'r', '狊': 's', '狋': 't', '狌': 'u', '狏': 'v', '狑': 'w',
    '狓': 'x', '狔': 'y', '狕': 'z',
    'Ａ': 'A', 'Ｂ': 'B', 'Ｃ': 'C', 'Ｄ': 'D', 'Ｅ': 'E', 'Ｆ': 'F', 'Ｇ': 'G',
    'Ｈ': 'H', 'Ｉ': 'I', 'Ｊ': 'J', 'Ｋ': 'K', 'Ｌ': 'L', 'Ｍ': 'M', 'Ｎ': 'N',
    'Ｏ': 'O', 'Ｐ': 'P', 'Ｑ': 'Q', 'Ｒ': 'R', 'Ｓ': 'S', 'Ｔ': 'T', 'Ｕ': 'U',
    'Ｖ': 'V', 'Ｗ': 'W', 'Ｘ': 'X', 'Ｙ': 'Y', 'Ｚ': 'Z',
    '０': '0', '１': '1', '２': '2', '３': '3', '４': '4', '５': '5', '６': '6',
    '７': '7', '８': '8', '９': '9',
    '．': '.', '－': '-', '：': ':', '，': ',', '；': ';', '！': '!', '？': '?',
    '（': '(', '）': ')', '【': '[', '】': ']', '《': '<', '》': '>',
}


def decode_fullwidth(text):
    """Decode full-width and pseudo-English characters."""
    result = []
    for char in text:
        if char in PSEUDO_ENGLISH_MAP:
            result.append(PSEUDO_ENGLISH_MAP[char])
        else:
            result.append(char)
    return ''.join(result)


def extract_text_from_pdf(pdf_path):
    """Extract all text from PDF file using pdftotext."""
    try:
        subprocess.run(
            ['pdftotext', pdf_path, '/tmp/pdf_text.txt'],
            capture_output=True,
            text=True,
            check=True
        )
        with open('/tmp/pdf_text.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error extracting PDF: {e}")
        return None


def parse_hierarchical_terms(text):
    """
    Parse hierarchical terms from PDF text.
    Extract terms from section 3.1 to 5.3.38 with 3-layer structure.
    """
    result = {}
    lines = text.split('\n')
    i = 0
    
    while i < len(lines):
        # Check for 3-line term ID pattern
        if i + 2 < len(lines):
            line1 = lines[i].strip()
            line2 = lines[i+1].strip()
            line3 = lines[i+2].strip()
            
            # Pattern: "５．" + "３．" + "３８" (or "１" for single digit)
            if re.match(r'^[０-９]+[．\.]$', line1):
                if re.match(r'^[０-９]+[．\.]?$', line2):
                    if re.match(r'^[０-９]+$', line3):
                        term_id = decode_fullwidth(f"{line1}{line2}{line3}")
                        # Fix the pattern: "5．" + "3．" + "38" -> "5.3.38"
                        term_id = term_id.replace('．.', '.')
                        term_id = term_id.replace('..', '.')
                        
                        if is_in_range(term_id):
                            cn_name, en_name, new_i = extract_names_from_lines(lines, i + 3)
                            
                            if cn_name:
                                section_title = get_section_title_from_id(term_id)
                                add_to_hierarchy(result, term_id, cn_name, en_name, section_title)
                                print(f"Extracted: {term_id} {cn_name} | {en_name}")
                                i = new_i
                                continue
        
        i += 1
    
    return result


def extract_names_from_lines(lines, start_idx):
    """Extract Chinese and English names starting from given line index."""
    cn_name = None
    en_letters = []
    i = start_idx
    max_lines = 30
    
    while i < len(lines) and i < start_idx + max_lines:
        line = lines[i].strip()
        
        if not line:
            i += 1
            continue
        
        # Check if we've reached a new term
        if re.match(r'^[０-９]+[．\.]?$', line):
            break
        
        # Check for Chinese characters (excluding pseudo-English range)
        has_real_chinese = any('\u4e00' <= c <= '\u9fff' and '\u72A0' > c or c > '\u72FF' 
                               for c in line)
        has_pseudo_english = any('\u72A0' <= c <= '\u72FF' for c in line)
        
        # Extract Chinese name (first line with Chinese after term ID)
        if cn_name is None and has_real_chinese:
            # Extract only Chinese part
            cn_match = re.match(r'^([^\u72A0-\u72FF]+)', line)
            if cn_match:
                cn_name = cn_match.group(1).strip()
        
        # Collect pseudo-English letters
        if has_pseudo_english and not has_real_chinese:
            # Each line typically has 1-2 letters
            decoded = decode_fullwidth(line)
            letters = re.sub(r'[^a-zA-Z]', '', decoded)
            en_letters.append(letters)
        
        # If we hit a line with real Chinese and no pseudo-English, it's likely the definition
        if has_real_chinese and not has_pseudo_english and cn_name:
            break
        
        i += 1
    
    # Combine English letters (they should read horizontally when concatenated)
    en_name = ''.join(en_letters)
    
    return cn_name, en_name, i


def get_section_title_from_id(term_id):
    """Get section title based on term ID."""
    parts = term_id.split('.')
    if len(parts) >= 1:
        section_num = parts[0]
        section_map = {
            '3': '一般术语',
            '4': '典型表面加工术语',
            '5': '冷作、钳工及装配常用术语'
        }
        return section_map.get(section_num, '')
    return ''


def is_in_range(term_id):
    """Check if term ID is in range 3.1 to 5.3.38."""
    try:
        parts = term_id.split('.')
        major = int(parts[0])
        
        if major < 3 or major > 5:
            return False
        
        if major == 3:
            if len(parts) < 2:
                return False
            minor = int(parts[1])
            return minor >= 1
        
        if major == 4:
            return True
        
        if major == 5:
            if len(parts) < 2:
                return False
            minor = int(parts[1])
            if minor < 3:
                return False
            if minor == 3 and len(parts) >= 3:
                sub_minor = int(parts[2])
                return sub_minor <= 38
            return True
        
        return True
    except (ValueError, IndexError):
        return False


def add_to_hierarchy(result, term_id, cn_name, en_name, section_title):
    """Add term to hierarchical structure."""
    parts = term_id.split('.')
    
    # Get section key
    section_num = parts[0]
    section_key = f"{section_num} {section_title}" if section_title else section_num
    
    # Create section if doesn't exist
    if section_key not in result:
        result[section_key] = {}
    
    if len(parts) == 2:
        # Two-level structure (e.g., 3.1)
        level2 = term_id
        
        if level2 not in result[section_key]:
            result[section_key][level2] = {}
        
        result[section_key][level2][term_id] = {
            "CnName": cn_name,
            "EnName": en_name
        }
    
    elif len(parts) == 3:
        # Three-level structure (e.g., 5.3.38)
        level2 = f"{parts[0]}.{parts[1]}"
        level3 = term_id
        
        if level2 not in result[section_key]:
            result[section_key][level2] = {}
        
        result[section_key][level2][level3] = {
            "CnName": cn_name,
            "EnName": en_name
        }


def save_to_json(data, output_path):
    """Save data to JSON file with proper formatting."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    # Define file paths
    pdf_path = "/workspace/zbackup/sources/4863-2008-gbt-e-300机械制造工艺基本术语.pdf"
    output_path = "/workspace/dlake/gov/stdgb/CCSA22/41923-3dprocess.json"
    
    # Extract text from PDF
    print(f"Reading PDF: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)
    
    if not text:
        print("Failed to extract text from PDF")
        return
    
    print(f"Extracted {len(text)} characters from PDF\n")
    
    # Parse hierarchical terms
    print("Parsing hierarchical terms...")
    result = parse_hierarchical_terms(text)
    
    if not result:
        print("No terms found in specified range")
        return
    
    # Save to JSON
    print(f"\nSaving to JSON: {output_path}")
    save_to_json(result, output_path)
    
    print(f"\nSuccessfully extracted {len(result)} main sections")
    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    main()
