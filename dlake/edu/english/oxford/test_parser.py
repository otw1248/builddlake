# Created by AI Assistant on 2026-01-19
"""
Test script for Oxford Dictionary Parser - Simplified
"""

from oxford_parser import OxfordDictionaryParser
import json

def test_parser():
    parser = OxfordDictionaryParser()
    
    # Create a small test file
    test_content = """A-  prefix (also an- before a vowel sound) not, without (amoral). [greek]

Aa  abbr. 1 automobile association. 2 alcoholics anonymous. 3 anti-aircraft.

Aardvark  n. Mammal with a tubular snout and a long tongue, feeding on termites. [afrikaans]

Ab-  prefix off, away, from (abduct). [latin]

Aback  adv.  take aback surprise, disconcert. [old english: related to *a2]

Abacus  n. (pl. -cuses) 1 frame with wires along which beads are slid for calculating. 2 archit. Flat slab on top of a capital. [latin from greek from hebrew]

Abaft  naut. —adv. In the stern half of a ship. —prep. Nearer the stern than. [from *a2, -baft: see *aft]

Abandon  —v. 1 give up. 2 forsake, desert. 3 (often foll. By to; often refl.) Yield to a passion, another's control, etc. —n. Freedom from inhibitions.  abandonment n. [french: related to *ad-, *ban]

Abandoned  adj. 1 deserted, forsaken. 2 unrestrained, profligate.

Abase  v. (-sing) (also refl.) Humiliate, degrade.  abasement n. [french: related to *ad-, *base2]
"""
    
    # Write test file
    test_file = '/workspace/dlake/edu/english/oxford/test_sample.txt'
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    print("Testing parser with sample data...")
    
    # Parse the test file
    data = parser.parse_file(test_file)
    
    print(f"Total entries parsed: {data['total_entries']}")
    
    # Display some entries
    for i, entry in enumerate(data['entries'][:5]):
        print(f"\n--- Entry {i+1}: {entry['word']} ---")
        print(json.dumps(entry, ensure_ascii=False, indent=2))
    
    # Save to JSON for inspection
    output_file = '/workspace/dlake/edu/english/oxford/test_output.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Test output saved to {output_file}")
    print("✓ Test complete!")

if __name__ == '__main__':
    test_parser()
