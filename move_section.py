import os
import re

dir_path = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
inv_file = os.path.join(dir_path, "investment-criteria.html")
idx_file = os.path.join(dir_path, "index.html")

# 1. Read investment-criteria.html
with open(inv_file, "r", encoding="utf-8") as f:
    inv_content = f.read()

# 2. Extract Key Strengths section using regex
pattern = r"(\s*<!-- ===== KEY STRENGTHS SECTION ===== -->[\s\S]*?</section>)"
match = re.search(pattern, inv_content)

if match:
    section_html = match.group(1)
    
    # Remove from investment-criteria.html
    new_inv_content = inv_content.replace(section_html, "")
    with open(inv_file, "w", encoding="utf-8") as f:
        f.write(new_inv_content)
    
    # 3. Read index.html
    with open(idx_file, "r", encoding="utf-8") as f:
        idx_content = f.read()
    
    # Insert before CTA section
    cta_marker = r"(\s*<!-- ===== CTA SECTION ===== -->)"
    new_idx_content = re.sub(cta_marker, section_html + r"\n\1", idx_content)
    
    # Ensure CTA image is updated
    new_idx_content = new_idx_content.replace('images/cta-bg.png', 'images/vXr_lets-connect.jpeg')
    
    with open(idx_file, "w", encoding="utf-8") as f:
        f.write(new_idx_content)
        
    print("Section successfully moved and index.html updated.")
else:
    print("Could not find the section in investment-criteria.html")
