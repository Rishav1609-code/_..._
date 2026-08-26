import os
import re

file_path = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\styles.css"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We will replace from .family-funds { to .metric-label { ... }
target_regex = re.compile(
    r'\.family-funds \{.*?\.metric-label \{.*?\}',
    re.DOTALL
)

replacement = """
.family-funds {
    position: absolute;
    bottom: 24px;
    left: 24px;
    right: 24px;
    background: linear-gradient(145deg, rgba(30, 30, 30, 0.4) 0%, rgba(10, 10, 10, 0.6) 100%);
    backdrop-filter: blur(28px);
    -webkit-backdrop-filter: blur(28px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-top: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 28px;
    padding: 40px 48px;
    color: var(--color-white);
    box-shadow: 
        0 30px 60px rgba(0, 0, 0, 0.4),
        inset 0 1px 1px rgba(255, 255, 255, 0.1);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.family-left:hover .family-funds {
    transform: translateY(-5px);
    box-shadow: 
        0 40px 80px rgba(0, 0, 0, 0.5),
        inset 0 1px 1px rgba(255, 255, 255, 0.2);
}

.family-funds-title {
    font-size: 0.95rem;
    color: rgba(255, 255, 255, 0.75);
    margin-bottom: 24px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-weight: 500;
}

.family-funds-grid {
    display: flex;
    gap: 50px;
}

.fund-item {}

.fund-value {
    font-family: var(--font-heading);
    font-size: 3rem;
    font-weight: 700;
    display: flex;
    align-items: baseline;
    gap: 2px;
    line-height: 1;
    margin-bottom: 8px;
    color: #fff;
    text-shadow: 0 0 20px rgba(255,255,255,0.2);
}

.fund-label {
    font-size: 0.95rem;
    color: rgba(255, 255, 255, 0.85);
    font-weight: 400;
}

.family-right {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 50px;
    padding: 20px 0;
}

.family-right h2 {
    font-size: clamp(2.5rem, 4vw, 3.5rem);
    line-height: 1.1;
    color: var(--color-brown);
    font-weight: 700;
    margin-bottom: 24px;
}

.family-right p {
    color: var(--color-grey);
    max-width: 540px;
    font-size: 1.1rem;
    line-height: 1.7;
    margin-bottom: 32px;
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    padding-top: 40px;
    border-top: 1px solid rgba(78, 57, 46, 0.15);
}

.metric-item {}

.metric-value {
    font-family: var(--font-heading);
    font-size: clamp(2.5rem, 3.5vw, 3.5rem);
    font-weight: 700;
    display: flex;
    align-items: baseline;
    gap: 2px;
    line-height: 1;
    margin-bottom: 12px;
    background: linear-gradient(135deg, var(--color-brown) 0%, #8A6E59 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    opacity: 1;
}

.metric-label {
    font-size: 0.95rem;
    color: var(--color-grey);
    line-height: 1.5;
    font-weight: 500;
}
""".strip()

content_new, count = target_regex.subn(replacement, content)

if count == 0:
    print("Replacement failed! Target not found.")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content_new)
    print(f"Replacement successful! Replaced {count} instances.")
