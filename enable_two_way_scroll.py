import os
import glob
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

new_observer = """const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                } else {
                    entry.target.classList.remove('visible');
                }
            });
        }, { threshold: 0, rootMargin: '0px 0px -50px 0px' });"""

pattern = re.compile(r"const revealObserver = new IntersectionObserver\(\(entries\) => \{.*?\}(,\s*\{.*?\})?\);", re.DOTALL)

for filepath in html_files:
    if 'siwa_source.html' in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    content = pattern.sub(new_observer, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated two-way animations in {os.path.basename(filepath)}")
    else:
        print(f"No match found or unchanged in {os.path.basename(filepath)}")
