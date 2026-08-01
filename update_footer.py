import os
import glob
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

new_text = "vXr Holdings is a next-generation technology group engineering a unified digital ecosystem. We deliver secure, thoroughly verified platforms designed to bridge the gap between digital innovation and real-world convenience."

pattern = re.compile(r'(<p class="footer-description">)(.*?)(</p>)', re.DOTALL)

for filepath in html_files:
    if 'siwa_source.html' in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    content = pattern.sub(r'\g<1>' + new_text + r'\g<3>', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated footer description in {os.path.basename(filepath)}")
