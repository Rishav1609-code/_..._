import os

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_path = os.path.join(dir_path, 'services.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

replacements = {
    4: ("vXr_Nexus", "services_pics/vXr_Nexus.png"),
    5: ("vXr_OneLink", "services_pics/vXr_OneLink.png"),
    6: ("vXr_TalentGrid", "services_pics/vXr_TalentGrid.png"),
    7: ("vXr_SafeDrop", "services_pics/vXr_SafeDrop.jpeg"),
    8: ("vXr_FileForge", "services_pics/vXr_FileForge.jpeg"),
    9: ("vXr_Haven", "services_pics/vXr_Haven.png"),
    10: ("vXr_Omni", "services_pics/vXr_Omni.png"),
    11: ("vXr_Infra", "services_pics/vXr_Infra.png"),
}

for i, (title, img_path) in replacements.items():
    title_placeholder = f"<h2>Service Title {i:02d}</h2>"
    new_title = f"<h2>{title}</h2>"
    html_content = html_content.replace(title_placeholder, new_title)
    
    img_placeholder = f'img src="images/FOR_our_service.jpeg" alt="Service {i} Image"'
    new_img = f'img src="{img_path}" alt="{title}"'
    html_content = html_content.replace(img_placeholder, new_img)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated services 4 through 11 successfully.")
