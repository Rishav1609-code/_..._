import os
import re

directory = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE"
html_file = os.path.join(directory, "index.html")
css_file = os.path.join(directory, "styles.css")

# 1. Update HTML
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

new_arrow = """<span class="icon-arrow-dynamic">
                                <span class="arrow-current">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none">
                                        <path d="M6.5 3.5h6v6" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round" />
                                        <path d="M12.5 3.5L3.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </span>
                                <span class="arrow-next">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none">
                                        <path d="M6.5 3.5h6v6" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round" />
                                        <path d="M12.5 3.5L3.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </span>
                            </span>"""

# We'll use regex to replace all <span class="icon-arrow"> ... </span>
pattern = r'<span class="icon-arrow">[\s\S]*?</span>'
html_content = re.sub(pattern, new_arrow, html_content)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

# 2. Update CSS
with open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

dynamic_arrow_css = """
/* Dynamic Arrow Hover Effect */
.icon-arrow-dynamic {
    position: relative;
    display: inline-flex;
    overflow: hidden;
    width: 16px;
    height: 16px;
    align-items: center;
    justify-content: center;
}
.arrow-current, .arrow-next {
    position: absolute;
    display: flex;
    width: 100%;
    height: 100%;
    transition: transform 0.4s cubic-bezier(0.76, 0, 0.24, 1);
}
.arrow-next {
    transform: translate(-100%, 100%);
}
.btn:hover .arrow-current, .btn-link:hover .arrow-current, .nav-cta a:hover .arrow-current {
    transform: translate(100%, -100%);
}
.btn:hover .arrow-next, .btn-link:hover .arrow-next, .nav-cta a:hover .arrow-next {
    transform: translate(0, 0);
}
.icon-arrow-dynamic svg {
    width: 100%;
    height: 100%;
}
"""

if ".icon-arrow-dynamic" not in css_content:
    css_content += "\n" + dynamic_arrow_css

    with open(css_file, "w", encoding="utf-8") as f:
        f.write(css_content)

print("Dynamic arrows updated successfully!")
