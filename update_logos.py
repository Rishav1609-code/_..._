import os
import re
import glob

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

# Patterns to match the old logos
# 1. Boot Logo
loader_pattern = r'<div class="loader-logo">.*?</div>'
new_loader = '''<div class="loader-logo" style="width: 220px; display: flex; justify-content: center; align-items: center;">
            <img src="images/logo-official.png" alt="vXr Holdings" style="width: 100%; height: auto; object-fit: contain;">
        </div>'''

# 2. Navbar Logo
navbar_pattern = r'<a href="index\.html" class="navbar-logo" id="navLogo">[\s\S]*?</a>'
new_navbar = '''<a href="index.html" class="navbar-logo" id="navLogo" style="display: flex; align-items: center; width: 140px; margin-top: -8px;">
                <img src="images/logo-official.png" alt="vXr Holdings" style="width: 100%; height: auto; object-fit: contain;">
            </a>'''

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace loader logo
    content = re.sub(loader_pattern, new_loader, content)
    
    # Replace navbar logo
    content = re.sub(navbar_pattern, new_navbar, content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated logos in {len(html_files)} HTML files.")
