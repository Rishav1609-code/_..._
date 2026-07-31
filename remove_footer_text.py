import os
import glob
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

pattern = r'<div class="footer-logo-bottom">VXR HOLDINGS</div>'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(pattern, '<div class="footer-logo-bottom"></div>', content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Removed text from {os.path.basename(file_path)}")

print("Footer text removal complete.")
