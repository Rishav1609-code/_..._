import os
import glob

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

for filepath in html_files:
    if 'siwa_source.html' in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    content = content.replace(">About Us<", ">About vXr<")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated 'About Us' to 'About vXr' in {os.path.basename(filepath)}")
