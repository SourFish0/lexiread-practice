import json 

def count_long_term_words(file_path: str) -> dict:
    """
    Counts the number of words with an interval longer than 365 days.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    word_list = data.get("words", [])
    container = []
    error_list = []

    for entry in word_list:
        interval = entry.get("interval", 0)
        word = entry.get("text", "Unknown Word")
        if not isinstance(interval, (int, float)):
            error_list.append(word)
            continue
        elif interval > 365:
            container.append(word)

    return {
        "total_words": len(word_list),
        "long_term_count": len(container),
        "sample_long_term_words": container[:3],
        "error_lists": error_list
    }



export = count_long_term_words("words.json")
display_text = f"""Your current vocabulary has {export['long_term_count']} words with an interval longer than 365 days, 
accounting for {export['long_term_count'] / export['total_words'] * 100:.2f}% of your total vocabulary. 
Sample long-term words: {', '.join(export['sample_long_term_words'])} 
{"Warning: The following entries had invalid interval values: {', '.join(export['error_lists'])}" if export['error_lists'] else ""}"""
print (display_text)