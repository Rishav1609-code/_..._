import re

html_file = 'portfolio.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

start_tag = '<div class="pf-cards-grid" id="pfCardsGrid">'
end_tag = '</div><!-- /pf-cards-grid -->'

start_idx = content.find(start_tag) + len(start_tag)
end_idx = content.find(end_tag)

new_grid = '''
            <!-- Company 1: Swoogo -->
            <div class="pf-card" data-deal="self-funded" data-sector="technology" data-year="2024" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#e86431; font-weight:800; font-size:4.2rem; font-family: 'Inter', sans-serif; letter-spacing:-0.05em; margin-top:0;">swoogo</div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Swoogo</h3>
                        <p>Industry-leading event management software simplifying the complexities of large-scale, enterprise, and hybrid events through an intuitive and customizable platform.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector:</em> Technology</span>
                            <span><em>Location:</em> US</span>
                            <span><em>Led by:</em> Leonora Valvo</span>
                            <span><em>Type:</em> Self Funded Search</span>
                            <span><em>Investment Date:</em> 2024</span>
                            <span><em>Status:</em> <span class="pf-badge current">Current</span></span>
                            <span><em>Website:</em> swoogo.events</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 2: Oakmont Education -->
            <div class="pf-card" data-deal="traditional-search" data-sector="education" data-year="2024" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#6d97b0; font-size:2.4rem; display:flex; align-items:center; gap:8px;">
                            <span style="font-size:1.3em;color:#6eb17e;margin-top:0;filter:drop-shadow(1px 2px 2px rgba(0,0,0,0.1));">🌳</span>
                            <div style="text-align:left;">
                                <div style="font-weight:700;">OAK<span style="font-weight:300;">MONT</span></div>
                                <span style="font-size:0.25em; letter-spacing:0.4em; display:block; color:#999; margin-top:1px; margin-left:2px; font-weight:500;">EDUCATION</span>
                            </div>
                        </div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Oakmont Education</h3>
                        <p>Providing specialized dropout recovery and alternative education programs for at-risk youth, empowering them with career technical training and high school diplomas.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector:</em> Education</span>
                            <span><em>Location:</em> Ohio, US</span>
                            <span><em>Led by:</em> Management Team</span>
                            <span><em>Type:</em> Traditional Search</span>
                            <span><em>Investment Date:</em> 2024</span>
                            <span><em>Status:</em> <span class="pf-badge current">Current</span></span>
                            <span><em>Website:</em> oakmont.edu</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 3: TelcoBridges -->
            <div class="pf-card" data-deal="self-funded" data-sector="technology" data-year="2024" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#2c2c2c; font-size:2.8rem;">TelcoBridges</div>
                    </div>
                    <div class="pf-card-back">
                        <h3>TelcoBridges</h3>
                        <p>A specialized developer and manufacturer of high-performance telecommunications hardware and software. TelcoBridges provides essential gateway solutions that enable interoperability between legacy and modern communication networks for clients worldwide.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector:</em> Technology</span>
                            <span><em>Location:</em> Quebec, Canada</span>
                            <span><em>Led by:</em> Maximilien Le Sieur</span>
                            <span><em>Type:</em> Self Funded Search</span>
                            <span><em>Investment Date:</em> 2024</span>
                            <span><em>Status:</em> <span class="pf-badge current">Current</span></span>
                            <span><em>Website:</em> telcobridges.com</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 4: OnPoint Generators -->
            <div class="pf-card" data-deal="independent-sponsor" data-sector="industrial" data-year="2024" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#2980b9; font-size:2rem; display:flex; align-items:center; justify-content:center; gap:12px;">
                            <span style="font-size:2.2em; margin-top:0; color:#3498db;">⟲</span>
                            <div style="text-align:left;">
                                <div style="font-weight:800; color:#1a3c63; font-size:1.3em; margin-bottom:-4px;">OnPoint</div>
                                <div style="font-weight:500; color:#3498db; font-size:0.9em; letter-spacing:0.02em;">Generators</div>
                            </div>
                        </div>
                    </div>
                    <div class="pf-card-back">
                        <h3>OnPoint Generators</h3>
                        <p>Specialized provider of industrial and commercial backup power generator sales, installation, and preventative maintenance services ensuring critical operations uptime.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector:</em> Industrial Services</span>
                            <span><em>Location:</em> US</span>
                            <span><em>Led by:</em> Operational Team</span>
                            <span><em>Type:</em> Independent Sponsor</span>
                            <span><em>Investment Date:</em> 2024</span>
                            <span><em>Status:</em> <span class="pf-badge current">Current</span></span>
                            <span><em>Website:</em> onpointgen.com</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 5: SabrePak -->
            <div class="pf-card" data-deal="long-term-hold" data-sector="business-services" data-year="2024" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#19278a; font-style:italic; font-weight:800; display:flex; align-items:center; gap:12px; font-size:2.2rem;">
                            SABREPAK <span style="font-size:1.5em; font-style:normal; margin-top:0; color:#19278a;">🐅</span>
                        </div>
                    </div>
                    <div class="pf-card-back">
                        <h3>SabrePak</h3>
                        <p>Innovative packaging solutions and logistics provider offering sustainable and custom protective packaging for industrial and commercial product shipping.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector:</em> Business Services</span>
                            <span><em>Location:</em> US</span>
                            <span><em>Led by:</em> Executive Team</span>
                            <span><em>Type:</em> Long Term Hold</span>
                            <span><em>Investment Date:</em> 2024</span>
                            <span><em>Status:</em> <span class="pf-badge current">Current</span></span>
                            <span><em>Website:</em> sabrepak.com</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 6: Paradosi Partners -->
            <div class="pf-card" data-deal="traditional-search" data-sector="search-fund" data-year="2024" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#333; font-size:2.8rem; font-weight:500;">Paradosi<br><span style="color:#666;">Partners</span></div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Paradosi Partners</h3>
                        <p>A traditional search fund led by two experienced mid-career professionals from Bain &amp; Company, seeking to acquire and operate a single high-quality business.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector:</em> Search Fund</span>
                            <span><em>Location:</em> Chicago and New York</span>
                            <span><em>Led by:</em> James Penz and Thu Ra</span>
                            <span><em>Type:</em> Traditional Search</span>
                            <span><em>Investment Date:</em> 2024</span>
                            <span><em>Status:</em> <span class="pf-badge current">Current</span></span>
                            <span><em>Website:</em> paradosipartners.com</span>
                        </div>
                    </div>
                </div>
            </div>
'''

new_content = content[:start_idx] + "\n" + new_grid + "\n        " + content[end_idx:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SUCCESS: Companies updated!")
