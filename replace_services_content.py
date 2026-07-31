import os
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
services_path = os.path.join(dir_path, 'services.html')
about_path = os.path.join(dir_path, 'about.html')

with open(about_path, 'r', encoding='utf-8') as f:
    about_content = f.read()

# Extract CTA from about.html
# It starts with <!-- ===== CTA SECTION ===== --> and ends with </section>\n        </div>\n\n        <!-- ===== FOOTER ===== -->
cta_match = re.search(r'(<!-- ===== CTA SECTION ===== -->.*?</div>\s*)(<!-- ===== FOOTER ===== -->)', about_content, re.DOTALL)
if not cta_match:
    print("Could not find CTA section in about.html")
    exit(1)

cta_section = cta_match.group(1)

with open(services_path, 'r', encoding='utf-8') as f:
    services_content = f.read()

# Replace SERVICES CONTENT with CTA
# It starts with <!-- ===== SERVICES CONTENT ===== --> and ends before <!-- ===== FOOTER ===== -->
services_content = re.sub(
    r'<!-- ===== SERVICES CONTENT ===== -->.*?<!-- ===== FOOTER ===== -->',
    cta_section + '<!-- ===== FOOTER ===== -->',
    services_content,
    flags=re.DOTALL
)

with open(services_path, 'w', encoding='utf-8') as f:
    f.write(services_content)

print("Removed services content and added CTA.")
