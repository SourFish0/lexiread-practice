import json

def check_review_health(file_path: str) -> dict:
    """
    Analyzes vocabulary data to identify 'leech' words with high failure rates.
    
    Parameters:
        file_path (str): Path to words.json.
        
    Returns:
        dict: Summary statistics including leech count and a sample list.
    """
    if not isinstance(file_path, str):
        raise TypeError(f"file_path must be a string, got {type(file_path).__name__}")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    word_list = data.get("words", [])
    total_words = len(word_list)

    # 1. Initialize our filter list
    leeches = []

    # 2. Filter for failure threshold
    for entry in word_list:
        fail_count = entry.get("failCount", 0)
        
        if isinstance(fail_count, (int, float)) and fail_count >= 2:
            # Save just the word and its failure count for reporting
            leeches.append({
                "text": entry.get("text", "UNKNOWN"),
                "fail_count": fail_count
            })

    # 3. Calculate health percentage
    leech_count = len(leeches)
    leech_rate = (leech_count / total_words * 100) if total_words > 0 else 0.0

    return {
        "total_words": total_words,
        "leech_count": leech_count,
        "leech_rate_percent": round(leech_rate, 2),
        "leeches": leeches
    }


# --- Execution Entry Point ---
report = check_review_health("words.json")

print("=== LexiRead Review Health Report ===")
print(f"Total Words Analyzed : {report['total_words']}")
print(f"Leeches Identified   : {report['leech_count']}")
print(f"Leech Rate           : {report['leech_rate_percent']}%")

# Display the first 5 troublesome words (List Slicing)
print("\n--- Top Leech Samples ---")
for item in report["leeches"][:5]:
    print(f"- {item['text']} (Failed {item['fail_count']} times)")