print(">>> DIAGNOSTIC: THE SCRIPT IS DEFINITELY RUNNING <<<")

import json

def count_vocab(file_path):
    """counts the number of mastered, learning, and new words in a JSON file."""
    # Raise
    if not isinstance(file_path, str):
        raise TypeError(f"file_path must be a string, got {type(file_path).__name__}")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    # Raise
    if not isinstance(data, dict):
        raise TypeError(f"JSON data must be a dictionary at the top level, got {type(data).__name__}")
    if "words" not in data:
        raise KeyError("JSON data must contain a 'words' key.")
    
    word_list = data.get("words", [])
    # Raise 
    if not isinstance(word_list, list):
        raise TypeError(f"'words' must be a list, got {type(word_list).__name__}")

    mastered_count = 0
    learning_count = 0
    new_count = 0

    for entry in word_list:
        familiarity = entry.get("familiarity", 0)

        if familiarity == 5:
            mastered_count += 1
        elif familiarity in [2, 3, 4]:
            learning_count += 1
        else:
            new_count += 1

    return {
        "total": len(word_list),
        "mastered": mastered_count,
        "learning": learning_count,
        "new": new_count
    }


# --- Execution Entry Point ---
stats = count_vocab("words.json")

print("=== LexiRead Vocabulary Statistics ===")
print(f"Total Words : {stats['total']}")
print(f"Mastered    : {stats['mastered']}")
print(f"Learning    : {stats['learning']}")
print(f"New         : {stats['new']}")