import glob
import os
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Footer link
    content = re.sub(
        r'<a href="#" class="footer-link-item">Champaran, Bihar, INDIA</a>',
        r'<a href="https://en.wikipedia.org/wiki/Champaran" target="_blank" rel="noopener noreferrer" class="footer-link-item">Champaran, Bihar, INDIA</a>',
        content
    )
    
    # 2. Mobile menu link
    content = re.sub(
        r'<a href="#" class="mobile-contact-link">(\s*<svg.*?</svg>\s*Champaran, Bihar, INDIA\s*)</a>',
        r'<a href="https://en.wikipedia.org/wiki/Champaran" target="_blank" rel="noopener noreferrer" class="mobile-contact-link">\1</a>',
        content,
        flags=re.DOTALL
    )

    # 3. Contact page specific
    content = re.sub(
        r'<div class="contact-method-text">Champaran, Bihar, INDIA</div>',
        r'<div class="contact-method-text"><a href="https://en.wikipedia.org/wiki/Champaran" target="_blank" rel=\"noopener noreferrer" style="color: inherit; text-decoration: none;">Champaran, Bihar, INDIA</a></div>',
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated links!')
