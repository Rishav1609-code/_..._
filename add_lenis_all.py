import os
import glob

dir_path = r'c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

lenis_script = """
    <!-- Smooth Scrolling (Lenis) -->
    <script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.29/bundled/lenis.min.js"></script>
    <script>
        const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), 
            direction: 'vertical', 
            gestureDirection: 'vertical',
            smooth: true,
            mouseMultiplier: 1,
            smoothTouch: false,
            touchMultiplier: 2,
            infinite: false,
        })

        function raf(time) {
            lenis.raf(time)
            requestAnimationFrame(raf)
        }

        requestAnimationFrame(raf)
    </script>
</body>"""

for filepath in html_files:
    if os.path.basename(filepath) in ['services.html', 'siwa_source.html']:
        continue # Already added or not needed
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "<!-- Smooth Scrolling (Lenis) -->" not in content:
        parts = content.rsplit('</body>', 1)
        if len(parts) == 2:
            new_content = parts[0] + lenis_script + parts[1]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added Lenis to {os.path.basename(filepath)}")
        else:
            print(f"Could not find </body> in {os.path.basename(filepath)}")
