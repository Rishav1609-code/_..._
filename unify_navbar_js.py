import os
import glob
import re

dir_path = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_files = glob.glob(os.path.join(dir_path, "*.html"))

new_js = """        // Navbar scroll effect
        const navbar = document.getElementById('navbar');
        let lastScroll = 0;
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            
            // Add scrolled class for background and padding changes
            if (scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }

            // Auto-hide navigation on scroll down
            if (scrollY > lastScroll && scrollY > 150) {
                // Scrolling down - hide navbar
                navbar.style.transform = 'translateY(-150%)';
                navbar.style.opacity = '0';
            } else {
                // Scrolling up - show navbar
                navbar.style.transform = 'translateY(0)';
                navbar.style.opacity = '1';
            }

            lastScroll = scrollY;
        });"""

# The regex will match from "// Navbar scroll effect" to the end of the event listener
pattern = re.compile(r"// Navbar scroll effect[\s\S]*?lastScroll = scrollY;\s*\}\);")

for file_path in html_files:
    if os.path.basename(file_path) == "index.html":
        # index.html already has the correct one, but just to be sure we can apply it too
        pass
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if re.search(pattern, content):
        new_content = re.sub(pattern, new_js, content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
print("Unified navbar scroll effect across all HTML files.")
