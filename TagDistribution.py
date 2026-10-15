import json

def generate_vocab_documentation(input_json: str, output_md: str):
    """
    Reads LexiRead words.json and generates an automated 
    Markdown status report (Docs-as-Code pipeline).
    """
    # 1. Load data
    with open(input_json, "r", encoding="utf-8") as file:
        data = json.load(file)

    tag_registry = data.get("tags", {})
    word_list = data.get("words", [])
    total_words = len(word_list)

    # 2. Compute Metrics
    leech_count = 0
    tag_counter = {}

    for entry in word_list:
        # A. Check for leeches (failCount >= 2)
        if entry.get("failCount", 0) >= 2:
            leech_count += 1

        # B. Tally tags
        word_tags = entry.get("tags", [])
        if not word_tags:
            tag_counter["Untagged"] = tag_counter.get("Untagged", 0) + 1
        else:
            for tag_id in word_tags:
                tag_name = tag_registry.get(tag_id, {}).get("name", "Unknown Tag")
                tag_counter[tag_name] = tag_counter.get(tag_name, 0) + 1

    leech_rate = (leech_count / total_words * 100) if total_words > 0 else 0.0

    # 3. Write Documentation Artifact (Markdown)
    with open(output_md, "w", encoding="utf-8") as doc:
        doc.write("# LexiRead Vocabulary Status Report\n\n")
        doc.write("> *Automated report generated from `words.json` via Docs-as-Code pipeline.*\n\n")
        
        doc.write("## 1. Library Health Overview\n")
        doc.write(f"* **Total Words Analyzed:** {total_words:,}\n")
        doc.write(f"* **At-Risk Words (Leeches):** {leech_count} ({leech_rate:.2f}%)\n\n")

        doc.write("## 2. Tag Distribution\n\n")
        doc.write("| Tag Category | Word Count |\n")
        doc.write("| :--- | :--- |\n")
        for tag, count in tag_counter.items():
            doc.write(f"| {tag} | {count:,} |\n")

    print(f"✅ Success: Documentation report written to '{output_md}'")


# --- Run the Pipeline ---
generate_vocab_documentation("words.json", "VOCAB_REPORT.md")