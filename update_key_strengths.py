import os
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
idx_file = os.path.join(directory, "index.html")
css_file = os.path.join(directory, "styles.css")

# 1. Update index.html
with open(idx_file, "r", encoding="utf-8") as f:
    idx_content = f.read()

# The exact old HTML block for this section
old_html_pattern = r'''<section class="section-key" id="strengths">[\s\S]*?</section>'''

new_html = '''<section class="section-key" id="strengths">
                <div class="key-bg">
                    <img src="images/KEY STRENGTHS SECTION_bg.jpeg" alt="Key Strengths Background" />
                    <div class="overlay" style="background: rgba(0,0,0,0.2);"></div>
                </div>
                <div class="container key-content">
                    <div class="key-header">
                        <h2 style="font-weight: 500; letter-spacing: -0.02em;">Key Strengths and Principles</h2>
                    </div>
                    <div class="key-cards">
                        <div class="key-card staggered-1" data-key-card>
                            <p>First-hand business experience<br>means we know what truly matters.</p>
                        </div>
                        <div class="key-card staggered-2" data-key-card>
                            <p>Capital invested alongside<br>yours for genuine alignment.</p>
                        </div>
                        <div class="key-card staggered-3" data-key-card>
                            <p>Quick action and open<br>communication at every stage.</p>
                        </div>
                    </div>
                </div>
            </section>'''

# Replace the HTML
if re.search(old_html_pattern, idx_content):
    idx_content = re.sub(old_html_pattern, new_html, idx_content)
    with open(idx_file, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("Updated HTML.")
else:
    print("Could not find section-key in HTML.")

# 2. Update styles.css
with open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

staggered_css = '''
/* Added staggered cascading effect for key cards */
.key-card.staggered-1 { margin-top: 0; }
.key-card.staggered-2 { margin-top: 60px; }
.key-card.staggered-3 { margin-top: 120px; }

@media (max-width: 768px) {
    .key-card.staggered-1, .key-card.staggered-2, .key-card.staggered-3 {
        margin-top: 0;
    }
}
'''

# Check if staggered CSS is already there
if "staggered-1" not in css_content:
    # Append staggered CSS after .key-card definition
    css_content = css_content.replace('.key-card p {', staggered_css + '\n.key-card p {')
    
    # Also adjust the padding-bottom of .section-key to accommodate the stagger
    if '.section-key {' not in css_content:
        # let's just add it
        css_content += "\n.section-key { padding-bottom: 200px; }\n"

    with open(css_file, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Updated CSS.")
else:
    print("CSS already updated.")
