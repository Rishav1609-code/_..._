import os
import glob
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))
index_file = os.path.join(directory, "index.html")

# 1. Read index.html to extract the new footer
with open(index_file, "r", encoding="utf-8") as f:
    index_content = f.read()

# Using regex to extract from <footer class="footer"> to </footer>
footer_match = re.search(r'(<footer class="footer">[\s\S]*?</footer>)', index_content)
if not footer_match:
    print("Could not find footer in index.html!")
    exit(1)

new_footer = footer_match.group(1)

# 2. Iterate through all other HTML files and replace their footer
for file_path in html_files:
    if os.path.basename(file_path) == "index.html":
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace old footer with new footer
    # Note: old footer might have a different class or formatting, but it should be a <footer> tag
    # Let's search for <footer ...> ... </footer>
    if '<footer' in content:
        new_content = re.sub(r'<footer[\s\S]*?</footer>', new_footer, content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated footer in {os.path.basename(file_path)}")
    else:
        print(f"No footer found in {os.path.basename(file_path)}")

print("Footer sync completed successfully!")
