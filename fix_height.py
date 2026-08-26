import os

files = [
    r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\about.html",
    r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\services.html",
    r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\portfolio.html",
    r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\investment-criteria.html"
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace 75vh with 100vh
    new_content = content.replace("min-height: 75vh;", "min-height: 100vh;")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated 4 files to min-height: 100vh.")
