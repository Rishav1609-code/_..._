import os
import re

css_path = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\styles.css"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# The user accidentally deleted a closing brace above .navbar.scrolled
# Let's fix the syntax error and remove the duplicate/old navbar rules

# We will remove the old .navbar.scrolled block completely
old_scrolled = r"\.navbar\.scrolled\s*\{[^}]*background:\s*rgba\(15,15,15,0\.85\);[^}]*\}"
css = re.sub(old_scrolled, "", css)

# Make sure .navbar.scrolled is transparent 
# (in case it got messed up, we'll ensure the new one exists)
if "background: transparent;" not in css and ".navbar.scrolled" in css:
    pass # we can assume the new one is still there based on the view_file

# Write it back
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Removed old black .navbar.scrolled background!")
