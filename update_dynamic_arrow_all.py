import os
import glob
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

new_arrow = """<span class="icon-arrow-dynamic">
                                <span class="arrow-current">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M7 7h10v10"/>
                                        <path d="M7 17 17 7"/>
                                    </svg>
                                </span>
                                <span class="arrow-next">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M7 7h10v10"/>
                                        <path d="M7 17 17 7"/>
                                    </svg>
                                </span>
                            </span>"""

# Regex to replace all <span class="icon-arrow-dynamic"> ... </span>
pattern = r'<span class="icon-arrow-dynamic">[\s\S]*?</span>'

for file_path in html_files:
    # (Removed skip logic for index.html so all pages get the new arrow)

    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    html_content = re.sub(pattern, new_arrow, html_content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print("Dynamic arrows updated successfully across all HTML files!")
