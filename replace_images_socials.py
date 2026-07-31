import glob
import os
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

for file_path in html_files:
    if os.path.basename(file_path) == 'siwa_source.html':
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Threads SVG with the image
    # We will use regex to find the entire <a href="#" class="social-icon" title="Threads"> ... </a> block
    content = re.sub(
        r'<a href="#" class="social-icon" title="Threads">.*?</a>',
        '<a href="#" class="social-icon" title="Threads">\n                        <img src="icons/threads_.png" alt="Threads" style="width: 20px; height: 20px; object-fit: contain; filter: contrast(0) sepia(1) hue-rotate(15deg) brightness(1.5) saturate(0.5); opacity: 0.7; transition: all 0.3s ease;" onmouseover="this.style.opacity=\'1\'; this.style.filter=\'contrast(0) sepia(1) hue-rotate(15deg) brightness(2) saturate(0.5)\'" onmouseout="this.style.opacity=\'0.7\'; this.style.filter=\'contrast(0) sepia(1) hue-rotate(15deg) brightness(1.5) saturate(0.5)\'" />\n                    </a>',
        content,
        flags=re.DOTALL
    )

    # 2. Replace Medium text with the image
    content = re.sub(
        r'<a href="#" class="social-icon" title="Medium">.*?</a>',
        '<a href="#" class="social-icon" title="Medium">\n                        <img src="icons/medium.jpeg" alt="Medium" style="width: 20px; height: 20px; object-fit: contain; filter: contrast(0) sepia(1) hue-rotate(15deg) brightness(1.5) saturate(0.5); opacity: 0.7; transition: all 0.3s ease; mix-blend-mode: screen;" onmouseover="this.style.opacity=\'1\'; this.style.filter=\'contrast(0) sepia(1) hue-rotate(15deg) brightness(2) saturate(0.5)\'" onmouseout="this.style.opacity=\'0.7\'; this.style.filter=\'contrast(0) sepia(1) hue-rotate(15deg) brightness(1.5) saturate(0.5)\'" />\n                    </a>',
        content,
        flags=re.DOTALL
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replaced Threads and Medium icons with images in all HTML files.")
