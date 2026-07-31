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
    content = content.replace("{ threshold: 0.15, rootMargin: '0px 0px -40px 0px' }", "{ threshold: 0, rootMargin: '0px 0px 150px 0px' }")
    content = content.replace("{ threshold: 0.2 }", "{ threshold: 0, rootMargin: '0px 0px 150px 0px' }")
    content = content.replace("{ threshold: 0.5 }", "{ threshold: 0, rootMargin: '0px 0px 50px 0px' }")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated IntersectionObservers in {os.path.basename(filepath)}")
