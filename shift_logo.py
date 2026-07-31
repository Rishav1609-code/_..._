import os
import glob

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

old_style = 'style="display: flex; align-items: center; width: 140px; margin-top: -8px;"'
new_style = 'style="display: flex; align-items: center; width: 140px; margin-top: -4px; margin-left: -20px;"'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_style in content:
        content = content.replace(old_style, new_style)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Shifted logo to the left in all HTML files.")
