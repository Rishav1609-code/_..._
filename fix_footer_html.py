import os
import glob
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    if os.path.basename(file_path) == "index.html":
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # We want the structure to be exactly:
    # </section>
    # </div> (closes id="top")
    # <footer class="footer"> ... </footer>
    # </div> <!-- End of App Wrapper -->
    
    # Let's clean up any weirdness between </section> and <footer class="footer">
    # Replace all whitespace, </div>s, and comments between the last </section> and <footer class="footer">
    # Actually, it's safer to just remove the extra </div> and <!-- ===== FOOTER ===== -->
    
    # We can use regex to fix:
    # </div>\s*<!-- ===== FOOTER ===== -->\s*</div>\s*<!-- ===== FOOTER ===== -->
    bad_pattern = r'</div>\s*<!-- ===== FOOTER ===== -->\s*</div>\s*<!-- ===== FOOTER ===== -->'
    if re.search(bad_pattern, content):
        content = re.sub(bad_pattern, r'</div>\n\n    <!-- ===== FOOTER ===== -->', content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed extra closing div in {os.path.basename(file_path)}")

print("Cleanup script done.")
