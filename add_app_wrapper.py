import os
import glob
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

wrapper_start = '''    <!-- App Wrapper for Framed Look -->
    <div class="app-wrapper">

    <!-- Navigation -->'''

wrapper_end = '''    </div> <!-- End of App Wrapper -->

    <script>'''

# Some files might have <!-- Scripts --> or something similar before <script>
# We'll just replace `<script>` with `wrapper_end` (assuming the last script tag or the main script block is what we find).
# But some files might have multiple script tags or it might be safer to replace `</body>` with `</div> </body>` if the script tags are inside the wrapper?
# Wait! In index.html, the script tag is OUTSIDE the app-wrapper. That means app-wrapper closes BEFORE <script>.
# Let's replace the first `<script>` occurrence with the closing div and then the `<script>`.

for file_path in html_files:
    if os.path.basename(file_path) == "index.html":
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if 'class="app-wrapper"' not in content:
        # Add opening tag
        content = content.replace("    <!-- Navigation -->", wrapper_start)
        
        # Add closing tag before the FIRST <script> tag
        # We can use regex to replace the first <script> with </div>\n<script>
        content = re.sub(r'(\s*<script>)', r'\n    </div> <!-- End of App Wrapper -->\n\1', content, count=1)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
print("App wrapper added to all remaining HTML files.")
