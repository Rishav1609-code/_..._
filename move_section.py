import os

about_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\about.html'
index_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\index.html'

with open(about_path, 'r', encoding='utf-8') as f:
    about_content = f.read()

start_marker = r'<!-- ===== ABOUT / FAMILY SECTION ===== -->'
end_marker = r'<!-- ===== TEAM SECTION ===== -->'

start_idx = about_content.find(start_marker)
end_idx = about_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    section_content = about_content[start_idx:end_idx]
    new_about_content = about_content[:start_idx] + about_content[end_idx:]
    with open(about_path, 'w', encoding='utf-8') as f:
        f.write(new_about_content)
        
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    insert_marker = r'<!-- ===== KEY STRENGTHS SECTION ===== -->'
    insert_idx = index_content.find(insert_marker)
    
    if insert_idx != -1:
        new_index_content = index_content[:insert_idx] + section_content + index_content[insert_idx:]
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_index_content)
        print("Successfully moved the section.")
    else:
        print("Could not find insert point in index.html.")
else:
    print("Could not find section in about.html.")
