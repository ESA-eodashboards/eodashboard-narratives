import os
import re
import json
import shutil

def extract_metadata(file_path):
    """Extracts first H1, first H3, and image URL from a Markdown file."""
    h1, h3, img_url = None, None, None
    
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if not h1:
                match_h1 = re.search(r'# (.+?)\s*<!--{.*?}-->', line)
                if match_h1:
                    h1 = match_h1.group(1)
            
            if not h3:
                match_h3 = re.search(r'### (.+?)\s*<!--{.*?}-->', line)
                if match_h3:
                    h3 = match_h3.group(1)

            if not img_url:
                match_img = re.search(r'<!--{.*?src="(.*?)".*?}-->', line)
                if match_img:
                    img_url = match_img.group(1)

            if h1 and h3 and img_url:
                break

    return {"file": file_path, "title": h1, "subtitle": h3, "image": img_url}

# Create output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Process all Markdown files
metadata_list = []
for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".md") and "scripts" not in root:
            file_path = os.path.join(root, file)
            metadata = extract_metadata(file_path)
            if metadata["title"] or metadata["subtitle"] or metadata["image"]:
                metadata_list.append(metadata)
            
            # Copy the markdown file to the output directory
            shutil.copy(file_path, os.path.join(output_dir, file))

# Save JSON metadata
with open(os.path.join(output_dir, "metadata.json"), "w", encoding="utf-8") as json_file:
    json.dump(metadata_list, json_file, indent=2, ensure_ascii=False)