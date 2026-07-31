import os
import re

css_file = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\styles.css"

with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

# 1. We will completely remove all existing `.navbar` and `.navbar.scrolled` blocks in the main CSS area.
# Because there are duplicates, we will use regex to remove them.

# Remove main .navbar blocks
css = re.sub(r'\.navbar\s*\{[^}]*\}', '', css)

# Remove main .navbar.scrolled blocks
css = re.sub(r'\.navbar\.scrolled\s*\{[^}]*\}', '', css)

# 2. Add our new perfect `.navbar` block.
new_navbar = """
/* ===== NAVBAR FIXED STABLE ===== */
.navbar {
    position: fixed;
    top: 40px;
    left: 40px;
    right: 40px;
    width: auto;
    z-index: 1000;
    padding: 0;
    transition: transform 0.4s cubic-bezier(0.65, 0, 0.35, 1), opacity 0.4s ease;
}

.navbar.scrolled {
    /* No size or position changes to prevent flickering! */
}
"""

# Insert it where the first navbar block used to be (roughly around .btn-glass)
css = css.replace('.btn-glass:hover {\n    background: rgba(255,255,255,0.1);\n    border-color: rgba(255,255,255,0.2);\n}', 
                  '.btn-glass:hover {\n    background: rgba(255,255,255,0.1);\n    border-color: rgba(255,255,255,0.2);\n}\n\n' + new_navbar)

# 3. Handle media queries
# Let's remove the .navbar padding changes in media queries that might cause flickering.
# The user wants NO resizing. Let's just remove .navbar.scrolled from media queries too.
css = re.sub(r'\.navbar\.scrolled\s*\{[^}]*\}', '', css)

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css)

print("Navbar styles updated to prevent flickering and resizing.")
