import os
import glob
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

# We want to remove the image tag with the class 'footer-giant-logo'
pattern = r'\s*<img src="LOGO/footer-bg-removed\.png" alt="vXr Holdings" class="footer-giant-logo">\s*'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(pattern, '\n', content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Removed giant logo from {os.path.basename(file_path)}")

print("Logo removal complete.")
