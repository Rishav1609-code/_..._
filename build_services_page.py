import glob
import os
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
about_path = os.path.join(dir_path, 'about.html')
services_path = os.path.join(dir_path, 'services.html')

with open(about_path, 'r', encoding='utf-8') as f:
    about_html = f.read()

# Create Services page structure
services_hero = """
        <!-- ===== SERVICES HERO ===== -->
        <section class="section-hero" id="hero" style="min-height: 60vh;">
            <div class="hero-bg">
                <img src="images/about-image.png" alt="Services Background" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(0.4);">
                <div class="hero-overlay"></div>
            </div>
            <div class="hero-content">
                <div class="hero-text-block" style="text-align: center; max-width: 800px; margin: 0 auto;">
                    <h1 class="hero-title reveal">Our Services</h1>
                    <p class="hero-subtitle reveal reveal-delay-1" style="font-size: 1.25rem;">Tailored solutions to elevate your enterprise. We provide strategic capital and operational expertise to drive long-term growth.</p>
                </div>
            </div>
        </section>

        <!-- ===== SERVICES CONTENT ===== -->
        <section class="section-padding" style="background: var(--color-bg); padding: 80px 20px;">
            <div class="container">
                <div class="services-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px;">
                    
                    <!-- Placeholder Service 1 -->
                    <div class="service-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 40px; transition: transform 0.3s ease;">
                        <h3 style="color: var(--color-cream); font-size: 1.5rem; margin-bottom: 20px; font-weight: 500;">Strategic Capital</h3>
                        <p style="color: rgba(255,255,255,0.7); font-size: 1rem; line-height: 1.6;">We provide flexible funding solutions tailored to the specific needs of high-growth enterprises and search funds.</p>
                    </div>

                    <!-- Placeholder Service 2 -->
                    <div class="service-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 40px; transition: transform 0.3s ease;">
                        <h3 style="color: var(--color-cream); font-size: 1.5rem; margin-bottom: 20px; font-weight: 500;">Operational Expertise</h3>
                        <p style="color: rgba(255,255,255,0.7); font-size: 1rem; line-height: 1.6;">Our team of seasoned operators brings hands-on experience to help optimize processes and scale your business.</p>
                    </div>

                    <!-- Placeholder Service 3 -->
                    <div class="service-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 40px; transition: transform 0.3s ease;">
                        <h3 style="color: var(--color-cream); font-size: 1.5rem; margin-bottom: 20px; font-weight: 500;">Long-term Partnership</h3>
                        <p style="color: rgba(255,255,255,0.7); font-size: 1rem; line-height: 1.6;">We build enduring relationships based on aligned incentives, shared vision, and mutual trust for sustained success.</p>
                    </div>

                </div>
            </div>
        </section>
"""

# Extract the part before <div id="top"> and the part after <!-- ===== FOOTER ===== -->
head_part = re.split(r'<div id="top">', about_html)[0] + '<div id="top">\n'
footer_part = '\n        <!-- ===== FOOTER ===== -->' + re.split(r'<!-- ===== FOOTER ===== -->', about_html)[1]

services_html = head_part + services_hero + footer_part

# Write services.html
with open(services_path, 'w', encoding='utf-8') as f:
    f.write(services_html)


# Now update all HTML files to include the links
html_files = glob.glob(os.path.join(dir_path, '*.html'))
for file_path in html_files:
    # Skip if it's not a real file
    if os.path.basename(file_path) == 'siwa_source.html':
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # If services.html is already in the nav, skip
    if 'href="services.html"' in content:
        continue

    # Navbar desktop link
    content = re.sub(
        r'<a href="about.html"\s*class="nav-link">About Us</a>',
        '<a href="about.html" class="nav-link">About Us</a>\n                <a href="services.html" class="nav-link">Our Services</a>',
        content
    )

    # Navbar mobile link
    content = re.sub(
        r'<a href="about.html"\s*class="nav-link-mobile"\s*onclick="closeMobileMenu\(\)">About Us</a>',
        '<a href="about.html" class="nav-link-mobile" onclick="closeMobileMenu()">About Us</a>\n                    <a href="services.html" class="nav-link-mobile" onclick="closeMobileMenu()">Our Services</a>',
        content
    )

    # Footer link
    content = re.sub(
        r'<a href="about.html"\s*class="footer-link-item">About</a>',
        '<a href="about.html" class="footer-link-item">About</a>\n                        <a href="services.html" class="footer-link-item">Our Services</a>',
        content
    )
    
    # Active class logic for services page
    if os.path.basename(file_path) == 'services.html':
        # Ensure title is correct
        content = re.sub(
            r'<title>.*?vXr Holdings.*?<\/title>',
            '<title>Our Services — vXr Holdings</title>',
            content
        )
        content = re.sub(
            r'<a href="services.html"\s*class="nav-link">Our Services</a>',
            '<a href="services.html" class="nav-link active">Our Services</a>',
            content
        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Services page created and links updated in all HTML files.")
