import os
import glob

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

old_path = 'images/logo-official.png'
new_path = 'LOGO/vXr_bg_removed_LOGO.png'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_path in content:
        content = content.replace(old_path, new_path)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print(f"Replaced {old_path} with {new_path} in HTML files.")
