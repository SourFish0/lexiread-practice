import json

def audit_missing_definitions(file_path):
    """Identifies vocabulary entries that lack definitions."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if 'words' not in data:
        raise KeyError("JSON data must contain a 'words' key.")

    word_list = data["words"]
    if not isinstance(word_list, list):
        raise TypeError(f"'words' must be a list, got {type(word_list).__name__}")

    # Accumulator: a list to store the words needing work
    missing_words = []

    for entry in word_list:
        word_text = entry.get("text", "UNKNOWN")
        definition = entry.get("definition", "").strip()

        # If definition is empty, collect this word
        if not definition:
            missing_words.append(word_text)

    return {
        "total_words": len(word_list),
        "missing_count": len(missing_words),
        "sample_words": missing_words[:5]  # The first 5 words as a quick sample
    }

# --- Execution ---
report = audit_missing_definitions("words.json")

print("=== Definition Coverage Audit ===")
print(f"Total Words     : {report['total_words']}")
print(f"Missing Defs    : {report['missing_count']}")
print(f"Sample to fix   : {report['sample_words']}")