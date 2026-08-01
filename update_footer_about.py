import os
import glob
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

pattern = re.compile(r'(<a href="about\.html" class="footer-link-item[^>]*>)About(</a>)')

for filepath in html_files:
    if 'siwa_source.html' in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    content = pattern.sub(r'\1About Us\2', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated About to About Us in {os.path.basename(filepath)}")
