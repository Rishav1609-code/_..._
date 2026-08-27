import glob
import re
import os

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'id="mobileClose"' in content and 'navbar-wrapper' in content:
        # Check if already moved
        if '<div class="mobile-toggles">' in content:
            continue
            
        # 1. Extract the mobile-close button
        close_btn_pattern = re.compile(r'\s*<button class="mobile-close" id="mobileClose" aria-label="Close menu">.*?</button>', re.DOTALL)
        match = close_btn_pattern.search(content)
        if not match:
            continue
        close_btn_html = match.group(0)
        
        # 2. Remove it from its current position
        new_content = content.replace(close_btn_html, '')
        
        # 3. Find the mobile-menu-toggle button
        toggle_btn_pattern = re.compile(r'(\s*<button class="mobile-menu-toggle" id="mobileToggle" aria-label="Open menu">.*?</button>)', re.DOTALL)
        
        # 4. Replace the toggle button with a wrapper containing both
        def replace_toggles(m):
            toggle_html = m.group(1)
            # We want them inside the navbar wrapper
            return '\n        <div class="mobile-toggles">' + toggle_html + close_btn_html + '\n        </div>'
            
        new_content = toggle_btn_pattern.sub(replace_toggles, new_content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
