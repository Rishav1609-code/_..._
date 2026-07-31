import os
import glob

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

for filepath in html_files:
    if 'siwa_source.html' in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    modified = False
    for i, line in enumerate(lines):
        if "}, { threshold: 0, rootMargin: '0px 0px 150px 0px' });" in line:
            if len(new_lines) > 0 and "-50px" in new_lines[-1]:
                print(f"Removed stray line in {os.path.basename(filepath)} at line {i+1}")
                modified = True
                continue 
        new_lines.append(line)
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
