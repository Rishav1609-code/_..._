import os

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
css_file = os.path.join(directory, "styles.css")

with open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

# Make .app-wrapper a flex container
if 'display: flex;\n    flex-direction: column;' not in css_content:
    css_content = css_content.replace(
        '.app-wrapper {\n    background-color: var(--color-black);',
        '.app-wrapper {\n    display: flex;\n    flex-direction: column;\n    background-color: var(--color-black);'
    )

# Make .footer push to the bottom
if 'margin-top: auto;' not in css_content:
    css_content = css_content.replace(
        '.footer {\n    background: var(--color-dark);',
        '.footer {\n    margin-top: auto;\n    background: var(--color-dark);'
    )

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css_content)

print("CSS updated to push footer to the bottom!")
