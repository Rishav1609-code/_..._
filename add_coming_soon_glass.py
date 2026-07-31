import os
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'

css_path = os.path.join(dir_path, 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

import_statement = "@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');\n"
if "family=Dancing+Script" not in css:
    css = import_statement + css

coming_soon_css = """
/* ===== COMING SOON OVERLAY ===== */
.coming-soon-wrapper {
    position: relative;
    width: 100%;
    margin-top: 10px;
    border-radius: 12px;
}

.coming-soon-overlay {
    position: absolute;
    top: -16px;
    left: -20px;
    right: -20px;
    bottom: -16px;
    background: rgba(255, 255, 255, 0.45);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.8);
    border-radius: 12px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
}

.coming-soon-text {
    font-family: 'Dancing Script', cursive;
    font-size: 3.8rem;
    color: var(--color-brown-dark);
    text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9);
    transform: rotate(-3deg);
    white-space: nowrap;
}
"""

if "coming-soon-overlay" not in css:
    css += coming_soon_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

html_path = os.path.join(dir_path, 'services.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(
    r'(<p>Detailed description of service number \d+ goes here\. This text explains the specific value proposition, operational methodologies, and expected outcomes that clients can anticipate\. Replace this placeholder text with your actual service details\.</p>\s*<a href="#contact"[^>]*>Learn More</a>)',
    re.DOTALL
)

replacement = r'''<div class="coming-soon-wrapper">
                            \1
                            <div class="coming-soon-overlay">
                                <span class="coming-soon-text">Coming Soon</span>
                            </div>
                        </div>'''

new_html = pattern.sub(replacement, html)

if new_html != html:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Added coming soon overlays to 9 services!")
else:
    print("No changes were made to services.html")
