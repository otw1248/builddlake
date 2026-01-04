import json

# Read both files
with open('/workspace/dlake/edu/english/pschool/unit-data-temp.json', 'r', encoding='utf-8') as f:
    temp_data = json.load(f)

with open('/workspace/dlake/edu/english/pschool/unit-data.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

# Merge: prepend temp data before main data
merged_data = {
    "words": temp_data['words'] + main_data['words'],
    "phrases": temp_data['phrases'] + main_data['phrases'],
    "sentences": temp_data['sentences'] + main_data['sentences']
}

# Write back to main file
with open('/workspace/dlake/edu/english/pschool/unit-data.json', 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=2)

# Print summary
print(f"Merge complete!")
print(f"\nSummary:")
print(f"  Words: {len(temp_data['words'])} (4-1) + {len(main_data['words'])} (4-2,5-1) = {len(merged_data['words'])} total")
print(f"  Phrases: {len(temp_data['phrases'])} (4-1) + {len(main_data['phrases'])} (4-2,5-1) = {len(merged_data['phrases'])} total")
print(f"  Sentences: {len(temp_data['sentences'])} (4-1) + {len(main_data['sentences'])} (4-2,5-1) = {len(merged_data['sentences'])} total")
