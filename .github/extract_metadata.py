import os
import re
import json
import sys
import yaml

# Get base URL from command-line argument or set a default
BASE_URL = sys.argv[1] if len(sys.argv) > 1 else "https://esa-eodash.github.io/eodashboard-narratives/"

def extract_metadata(file_path, base_url):
    """Extracts frontmatter metadata, first H1, first H3, and image URL from a Markdown file."""
    metadata = {}
    h1, h3, img_url = None, None, None
    filename = os.path.basename(file_path)
    file_url = base_url.rstrip("/") + "/" + filename  # Ensure proper URL format

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Extract frontmatter metadata (YAML-like block at the start)
    frontmatter_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if frontmatter_match:
        frontmatter_text = frontmatter_match.group(1)
        try:
            metadata = yaml.safe_load(frontmatter_text)  # Convert to dictionary
        except yaml.YAMLError:
            print(f"Warning: Could not parse frontmatter in {file_path}")

    # Extract first H1 header
    h1_match = re.search(r'# (.+?)\s*<!--{.*?}-->', content)
    if h1_match:
        h1 = h1_match.group(1)

    # Extract first H3 header
    h3_match = re.search(r'### (.+?)\s*<!--{.*?}-->', content)
    if h3_match:
        h3 = h3_match.group(1)

    # Extract first image URL
    img_match = re.search(r'<!--{.*?src="(.*?)".*?}-->', content)
    if img_match:
        img_url = img_match.group(1)

    # Merge extracted metadata
    metadata.update({
        "file": file_url,
        "title": h1,
        "subtitle": h3,
        "image": img_url
    })

    return metadata

# Create output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Process all Markdown files
metadata_list = []
for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".md") and "scripts" not in root:
            file_path = os.path.join(root, file)
            metadata = extract_metadata(file_path, BASE_URL)
            if any(metadata.values()):
                metadata_list.append(metadata)
                        

# Save JSON metadata
with open(os.path.join(output_dir, "narratives.json"), "w", encoding="utf-8") as json_file:
    json.dump(metadata_list, json_file, indent=2, ensure_ascii=False, default=str)