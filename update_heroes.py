import os
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'

files = {
    'about.html': {
        'old': r'<section class="section-sub-hero" id="hero">\s*<div class="hero-bg">\s*<img src="([^"]+)" alt="([^"]+)"\s*/>\s*<div class="hero-overlay"></div>\s*</div>\s*<div class="hero-content">\s*<h1 class="hero-title reveal">([^<]+)</h1>\s*</div>\s*</section>',
        'subtitle': 'Discover our story, values, and the driving force behind vXr Holdings.'
    },
    'investment-criteria.html': {
        'old': r'<section class="section-sub-hero" id="hero">\s*<div class="hero-bg">\s*<img src="([^"]+)" alt="([^"]+)"\s*/>\s*<div class="hero-overlay"></div>\s*</div>\s*<div class="hero-content">\s*<h1 class="hero-title reveal">([^<]+)</h1>\s*</div>\s*</section>',
        'subtitle': 'A disciplined strategy focused on sustainable growth and operational excellence.'
    },
    'portfolio.html': {
        'old': r'<section class="section-sub-hero" id="hero">\s*<div class="hero-bg">\s*<img src="([^"]+)" alt="([^"]+)"\s*/>\s*<div class="hero-overlay"></div>\s*</div>\s*<div class="hero-content">\s*<h1 class="hero-title reveal">([^<]+)</h1>\s*</div>\s*</section>',
        'subtitle': 'A diverse collection of high-performing enterprises shaping the future.'
    }
}

for filename, data in files.items():
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_hero(match):
        img_src = match.group(1)
        alt_text = match.group(2)
        title = match.group(3)
        return f'''<section class="section-hero" id="hero" style="min-height: 60vh;">
            <div class="hero-bg">
                <img src="{img_src}" alt="{alt_text}" style="width: 100%; height: 100%; object-fit: cover;">
                <div class="hero-overlay"></div>
            </div>
            <div class="hero-content">
                <div class="hero-text-block" style="text-align: center; max-width: 800px; margin: 0 auto;">
                    <h1 class="hero-title reveal">{title}</h1>
                    <p class="hero-subtitle reveal reveal-delay-1" style="font-size: 1.25rem;">{data["subtitle"]}</p>
                </div>
            </div>
        </section>'''

    new_content = re.sub(data['old'], replace_hero, content, count=1)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated heroes for all three pages.")
