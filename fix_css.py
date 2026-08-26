import os

file_path = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\styles.css"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """
.hero-content {
    position: relative;
    z-index: 2;
    width: 100%;
    height: 100%;
    align-items: flex-end;
    margin-bottom: 20px;
    opacity: 0;
    animation: heroFadeUp 0.8s 0.8s forwards cubic-bezier(0.22, 1, 0.36, 1);
}

.hero-stat-card {
    background: rgba(10, 10, 10, 0.4);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 40px 32px;
    text-align: left;
    min-width: 260px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.hero-stat-value {
    font-family: var(--font-heading);
    font-size: 3.5rem;
    font-weight: 500;
    color: var(--color-white);
    display: flex;
    align-items: baseline;
    line-height: 1;
    margin-bottom: 8px;
}

.hero-stat-label {
    font-size: 0.95rem;
    color: rgba(255, 255, 255, 0.7);
    text-transform: capitalize;
    letter-spacing: 0.02em;
}
"""

replacement = """
.hero-content {
    position: relative;
    z-index: 2;
    width: 100%;
    height: 100%;
    padding: 0 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.hero-stat-block {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    opacity: 0;
    animation: heroFadeUp 0.8s 0.8s forwards cubic-bezier(0.22, 1, 0.36, 1);
}

.hero-stat-card {
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.02) 100%);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 28px;
    padding: 40px 36px;
    text-align: left;
    min-width: 280px;
    box-shadow: 
        0 25px 50px rgba(0, 0, 0, 0.5),
        inset 0 1px 1px rgba(255, 255, 255, 0.4);
    transition: transform 0.5s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.5s ease, border-color 0.5s ease;
}

.hero-stat-card:hover {
    transform: translateY(-8px);
    box-shadow: 
        0 35px 70px rgba(0, 0, 0, 0.6),
        inset 0 1px 1px rgba(255, 255, 255, 0.6);
    border-color: rgba(255, 255, 255, 0.35);
}

.hero-stat-value {
    font-family: var(--font-heading);
    font-size: 4.5rem;
    font-weight: 700;
    color: #fff;
    display: flex;
    align-items: baseline;
    line-height: 1;
    margin-bottom: 12px;
    text-shadow: 0 0 30px rgba(255, 255, 255, 0.4);
}

.hero-stat-label {
    font-size: 1.05rem;
    color: rgba(255, 255, 255, 0.85);
    text-transform: capitalize;
    letter-spacing: 0.04em;
    font-weight: 400;
}
"""

# Handle potential newline differences
import re
target_regex = re.escape(target).replace(r'\n', r'\s+')
content_new = re.sub(target_regex, replacement.strip(), content)

if content == content_new:
    print("Replacement failed! Target not found.")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content_new)
    print("Replacement successful!")
