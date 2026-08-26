import sys

files = ['portfolio.html', 'investment-criteria.html', 'about.html', 'services.html']
for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'class="hero-content"' in content:
            content = content.replace('class="hero-content"', 'class="hero-content hero-content-center-override"', 1)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {filename}')
        else:
            print(f'Could not find hero-content in {filename}')
    except Exception as e:
        print(f'Error processing {filename}: {e}')
