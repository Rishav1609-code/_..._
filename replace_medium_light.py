import glob
import os

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

old_img = 'icons/medium.jpeg'
new_img = 'icons/medium_light.png'

for file_path in html_files:
    if os.path.basename(file_path) == 'siwa_source.html':
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_img in content:
        content = content.replace(old_img, new_img)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Replaced Medium icon to medium_light.png in all HTML files.")
