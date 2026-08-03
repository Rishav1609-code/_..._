import os
import glob
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(directory, "*.html"))

# Use regex to handle any potential newlines/whitespace differences across files
old_text = r"vXr Holdings is a next-generation technology group engineering a\s+unified digital ecosystem\.\s+We deliver secure,\s+thoroughly verified platforms designed to\s+bridge the gap between digital innovation and real-world convenience\."
new_text = "vXr Holdings develops next-generation, security-first platforms—seamlessly connecting digital innovation with the physical infrastructure of tomorrow."

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, num_subs = re.subn(old_text, new_text, content)
    
    if num_subs > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)} ({num_subs} replacements)")
    else:
        # Try a more forgiving regex if the first one missed
        old_text_loose = r"vXr Holdings is a next-generation technology group engineering a\s*unified digital ecosystem\.\s*We deliver secure, thoroughly verified platforms designed to\s*bridge the gap between digital innovation and real-world convenience\."
        new_content, num_subs = re.subn(old_text_loose, new_text, content)
        if num_subs > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)} ({num_subs} replacements) [using loose regex]")

