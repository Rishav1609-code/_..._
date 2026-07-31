import os
import glob
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

new_arrow = """<span class="icon-arrow-dynamic">
                                <span class="arrow-current">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none">
                                        <path d="M6.5 3.5h6v6" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round" />
                                        <path d="M12.5 3.5L3.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </span>
                                <span class="arrow-next">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none">
                                        <path d="M6.5 3.5h6v6" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round" />
                                        <path d="M12.5 3.5L3.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </span>
                            </span>"""

# Regex to replace all <span class="icon-arrow"> ... </span>
pattern = r'<span class="icon-arrow">[\s\S]*?</span>'

for file_path in html_files:
    if os.path.basename(file_path) == "index.html":
        # Skip index.html since it was already updated perfectly
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    html_content = re.sub(pattern, new_arrow, html_content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print("Dynamic arrows updated successfully across all HTML files!")
