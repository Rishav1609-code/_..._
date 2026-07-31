import os
import glob

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content.replace("Bihar, INDIA", "Champaran, Bihar, INDIA")

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated location in {os.path.basename(file_path)}")

print("Location update complete.")
