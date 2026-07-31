import glob
import os
import re

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'

socials_html = """
                <div class="footer-socials">
                    <a href="#" class="social-icon" title="LinkedIn">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
                            <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" title="X (Twitter)">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
                            <path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" title="YouTube">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
                            <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.5 12 3.5 12 3.5s-7.505 0-9.377.55a3.015 3.015 0 0 0-2.122 2.136C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.55 9.376.55 9.376.55s7.505 0 9.377-.55a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" title="Facebook">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
                            <path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" title="Instagram">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
                            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" title="Threads">
                        <!-- Threads @ icon approximation -->
                        <span style="font-family: sans-serif; font-weight: 700; font-size: 1.25rem;">@</span>
                    </a>
                    <a href="#" class="social-icon" title="Medium">
                        <!-- Medium M icon approximation -->
                        <span style="font-family: serif; font-weight: 700; font-size: 1.25rem;">M</span>
                    </a>
                </div>
"""

css_to_add = """
.footer-socials {
    display: flex;
    justify-content: flex-end;
    gap: 20px;
    padding-bottom: 24px;
}
.social-icon {
    color: rgba(241, 232, 217, 0.7);
    font-size: 1.2rem;
    text-decoration: none;
    transition: color 0.3s ease, transform 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}
.social-icon:hover {
    color: #ffffff;
    transform: translateY(-2px);
}
.social-icon svg {
    width: 20px;
    height: 20px;
    fill: currentColor;
}

@media (max-width: 768px) {
    .footer-socials {
        justify-content: center;
        padding-top: 32px;
    }
}
"""

html_files = glob.glob(os.path.join(dir_path, '*.html'))
for file_path in html_files:
    if os.path.basename(file_path) == 'siwa_source.html':
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already added
    if 'class="footer-socials"' in content:
        continue

    # Insert right before <div class="footer-bottom">
    content = content.replace('<div class="footer-bottom">', socials_html + '<div class="footer-bottom">')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update CSS
styles_path = os.path.join(dir_path, 'styles.css')
with open(styles_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.footer-socials' not in css_content:
    css_content += "\n" + css_to_add
    with open(styles_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

print('Added social icons successfully!')
