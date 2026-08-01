import os
import glob
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

def swap_links(content):
    pattern1 = re.compile(r'(<a href="about\.html" class="nav-link[^>]*>About Us</a>)(\s*)(<a href="services\.html" class="nav-link[^>]*>Our Services</a>)')
    content = pattern1.sub(r'\3\2\1', content)
    
    pattern2 = re.compile(r'(<a href="about\.html" class="nav-link-mobile[^>]*>About Us</a>)(\s*)(<a href="services\.html" class="nav-link-mobile[^>]*>Our Services</a>)')
    content = pattern2.sub(r'\3\2\1', content)

    pattern3 = re.compile(r'(<a href="about\.html" class="footer-link-item[^>]*>About(?: Us)?</a>)(\s*)(<a href="services\.html" class="footer-link-item[^>]*>Our Services</a>)')
    content = pattern3.sub(r'\3\2\1', content)
    
    return content

for filepath in html_files:
    if 'siwa_source.html' in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    content = swap_links(content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Swapped nav links in {os.path.basename(filepath)}")
    else:
        print(f"No match found in {os.path.basename(filepath)}")
