import os
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'

css_code = """
/* ===== SECTION: SERVICE SHOWCASE ===== */
.section-service-showcase {
    padding: 100px 0;
    background: var(--color-bg);
}

.service-row {
    display: flex;
    align-items: center;
    gap: 80px;
    margin-bottom: 120px;
}

.service-row:last-child {
    margin-bottom: 0;
}

.service-row.reverse {
    flex-direction: row-reverse;
}

.service-img-wrapper {
    flex: 0 0 50%;
    aspect-ratio: 16 / 9;
    border-radius: var(--radius-lg);
    overflow: hidden;
    position: relative;
    box-shadow: 0 24px 48px rgba(0,0,0,0.4);
    background: #111;
}

.service-img-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
}

.service-row:hover .service-img-wrapper img {
    transform: scale(1.05);
}

.service-content {
    flex: 1;
}

.service-content h2 {
    font-family: var(--font-heading);
    font-size: 2.5rem;
    font-weight: 300;
    color: var(--color-cream);
    margin-bottom: 24px;
    letter-spacing: -0.02em;
}

.service-content p {
    font-size: 1.15rem;
    color: rgba(241, 232, 217, 0.7);
    line-height: 1.6;
    margin-bottom: 32px;
}

@media (max-width: 768px) {
    .service-row, .service-row.reverse {
        flex-direction: column;
        gap: 40px;
        margin-bottom: 80px;
    }
    
    .service-img-wrapper {
        width: 100%;
        flex: none;
    }
    
    .service-content h2 {
        font-size: 2rem;
    }
}
"""

html_blocks = []
html_blocks.append('        <!-- ===== SERVICE SHOWCASE ===== -->\n        <section class="section-service-showcase">\n            <div class="container">')

placeholder_image = "images/FOR_our_service.jpeg"

for i in range(1, 10):
    is_reverse = " reverse" if i % 2 == 0 else ""
    html_blocks.append(f'''
                <!-- Service {i} -->
                <div class="service-row{is_reverse} reveal">
                    <div class="service-img-wrapper">
                        <img src="{placeholder_image}" alt="Service {i} Image">
                    </div>
                    <div class="service-content">
                        <h2>Service Title 0{i}</h2>
                        <p>Detailed description of service number {i} goes here. This text explains the specific value proposition, operational methodologies, and expected outcomes that clients can anticipate. Replace this placeholder text with your actual service details.</p>
                        <a href="#contact" class="btn btn-outline" style="border-color: rgba(241, 232, 217, 0.2); color: var(--color-cream);">Learn More</a>
                    </div>
                </div>''')

html_blocks.append('            </div>\n        </section>\n')
html_code = '\n'.join(html_blocks)

# Update CSS
css_path = os.path.join(dir_path, 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.section-service-showcase' not in css_content:
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content + '\n' + css_code)

# Update HTML
html_path = os.path.join(dir_path, 'services.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Insert before CTA
if '<!-- ===== SERVICE SHOWCASE ===== -->' not in html_content:
    html_content = html_content.replace('<!-- ===== CTA SECTION ===== -->', html_code + '\n        <!-- ===== CTA SECTION ===== -->')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("CSS and HTML successfully updated with 9 alternating services.")
