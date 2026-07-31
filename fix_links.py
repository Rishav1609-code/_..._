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

    # Check desktop navbar
    if 'href="services.html" class="nav-link"' not in content and 'href="services.html" class="nav-link active"' not in content:
        content = re.sub(
            r'(<a href="about\.html"[^>]*>About Us</a>)',
            r'\1\n                <a href="services.html" class="nav-link">Our Services</a>',
            content
        )
        
    # Check mobile menu
    if 'href="services.html" class="nav-link-mobile"' not in content:
        content = re.sub(
            r'(<a href="about\.html"[^>]*>About Us</a>)',
            r'\1\n                    <a href="services.html" class="nav-link-mobile" onclick="closeMobileMenu()">Our Services</a>',
            content
        )
        
    # Check footer
    if 'href="services.html" class="footer-link-item"' not in content:
        content = re.sub(
            r'(<a href="about\.html"[^>]*>About</a>)',
            r'\1\n                        <a href="services.html" class="footer-link-item">Our Services</a>',
            content
        )
        
    # Set active class specifically for services.html
    if os.path.basename(file_path) == 'services.html':
        content = re.sub(
            r'<a href="services\.html" class="nav-link">Our Services</a>',
            '<a href="services.html" class="nav-link active">Our Services</a>',
            content
        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Fixed missing links!')
