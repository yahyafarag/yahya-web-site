import os
import json
import fitz  # PyMuPDF
from collections import defaultdict
import re

directory = r"C:\Users\y_tar\Desktop\injaz &yahya for gpt"
index_file = "search_index.json"
markdown_artifact = "content_index.md"

word_index = defaultdict(list)
file_summaries = []

def extract_text_from_pdf(filepath):
    text = ""
    try:
        doc = fitz.open(filepath)
        for page in doc:
            text += page.get_text("text") + " "
        doc.close()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return text

def index_text(filepath, text):
    words = re.findall(r'\w+', text.lower())
    unique_words = set(words)
    rel_path = os.path.relpath(filepath, directory)
    for word in unique_words:
        word_index[word].append(rel_path)

print("Starting to index files...")

for root, _, files in os.walk(directory):
    for filename in files:
        filepath = os.path.join(root, filename)
        rel_path = os.path.relpath(filepath, directory)
        ext = os.path.splitext(filename)[1].lower()
        
        text = ""
        if ext == '.pdf':
            text = extract_text_from_pdf(filepath)
        elif ext in ['.md', '.txt']:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                
        if text:
            index_text(filepath, text)
            # Create a short summary for the markdown artifact
            summary = text[:200].replace('\n', ' ').strip() + "..."
            file_summaries.append(f"**{rel_path}**\n- *Type*: {ext.upper()}\n- *Preview*: {summary}\n")
        elif ext in ['.jpg', '.jpeg', '.png', '.webp']:
            file_summaries.append(f"**{rel_path}**\n- *Type*: Image\n")
        else:
            file_summaries.append(f"**{rel_path}**\n- *Type*: {ext.upper()}\n")

# Save JSON Index
with open(index_file, 'w', encoding='utf-8') as f:
    json.dump(word_index, f, ensure_ascii=False, indent=2)

print(f"Inverted index saved to {index_file} with {len(word_index)} unique words.")

# Save Markdown Summary
md_content = "# Knowledge Base Index 🗂️\n\nThis index maps out all files in the INJAZ project folder.\n\n"
md_content += "## 📄 Indexed Files & Previews\n\n"
for summary in file_summaries:
    md_content += summary + "\n"

with open(markdown_artifact, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Markdown summary saved to {markdown_artifact}.")
