import os
import glob
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

logo_html = """            </div>
            <div class="footer-full-width-logo">
                <img src="LOGO/footer-bg-removed-half.png" alt="vXr Holdings">
            </div>
        </footer>"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The HTML structure should currently be:
    #             </div> <!-- End of container inside footer, though there's no comment -->
    #         </footer>
    
    # Wait, the footer container is closed by `</div>\n        </footer>`
    # Let's match it safely
    pattern = r'(\s*)</div>\s*</footer>'
    
    # We will replace `            </div>\n        </footer>` with our logo_html
    # But wait, what if the spaces differ? Let's use re.sub
    
    new_content = re.sub(pattern, r'\1</div>\n            <div class="footer-full-width-logo">\n                <img src="LOGO/footer-bg-removed-half.png" alt="vXr Holdings">\n            </div>\n        </footer>', content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added full-width logo to {os.path.basename(file_path)}")

print("Logo addition complete.")
