import json

# Read the JSON file
with open('/workspace/dlake/edu/english/pschool/unit-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create a set of phrases (normalized - lowercase)
phrases_set = set()
for phrase in data['phrases']:
    phrases_set.add(phrase['phrase'].lower())

# Filter out sentences that match phrases
filtered_sentences = []
duplicates_found = []
for sentence in data['sentences']:
    sentence_text = sentence['sentence'].lower()
    if sentence_text in phrases_set:
        duplicates_found.append(sentence)
    else:
        filtered_sentences.append(sentence)

print(f"Found {len(duplicates_found)} duplicate sentences to remove:")
for dup in duplicates_found:
    print(f"  - {dup['sentence_id']}: {dup['sentence']}")

# Update the data
data['sentences'] = filtered_sentences

# Write back to file
with open('/workspace/dlake/edu/english/pschool/unit-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nRemaining sentences: {len(filtered_sentences)}")
print(f"Total phrases: {len(phrases_set)}")
