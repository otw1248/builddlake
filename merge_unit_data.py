#!/usr/bin/env python3
import json

# Read the main file
with open('/workspace/dlake/edu/english/pschool/unit-data.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

# Read the temp file
with open('/workspace/dlake/edu/english/pschool/unit-data-temp.json', 'r', encoding='utf-8') as f:
    temp_data = json.load(f)

# Merge words (prepend new words to existing ones)
main_data['words'] = temp_data['words'] + main_data['words']

# Merge phrases (prepend new phrases to existing ones)
main_data['phrases'] = temp_data['phrases'] + main_data['phrases']

# Merge sentences (prepend new sentences to existing ones)
main_data['sentences'] = temp_data['sentences'] + main_data['sentences']

# Write the merged data back to the main file
with open('/workspace/dlake/edu/english/pschool/unit-data.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged data:")
print(f"  Words: {len(temp_data['words'])} new words added (total: {len(main_data['words'])})")
print(f"  Phrases: {len(temp_data['phrases'])} new phrases added (total: {len(main_data['phrases'])})")
print(f"  Sentences: {len(temp_data['sentences'])} new sentences added (total: {len(main_data['sentences'])})")
