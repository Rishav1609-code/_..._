import os
import glob

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

old_src = 'images/cta-bg.png'
new_src = 'images/vXr_lets-connect.jpeg'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_src in content:
        content = content.replace(old_src, new_src)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print(f"Replaced {old_src} with {new_src} in HTML files.")
