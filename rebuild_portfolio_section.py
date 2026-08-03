import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start and end markers
start_marker = '<!-- ===== PORTFOLIO SECTION ===== -->'
end_marker = '<!-- ===== CTA SECTION ===== -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("ERROR: Markers not found!")
    print(f"Start found: {start_idx != -1}, End found: {end_idx != -1}")
    exit(1)

new_section = '''<!-- ===== PORTFOLIO SECTION ===== -->
<section class="section-portfolio-cards" id="portfolio-companies">
    <div class="container">

        <!-- Section Header + Filter -->
        <div class="pf-top-bar">
            <div class="pf-top-bar-left">
                <h2 class="pf-title reveal">Explore Our Investments</h2>
                <p class="pf-subtitle reveal">Browse our portfolio companies — filter by deal type, sector, year, or status.</p>
            </div>
            <div class="pf-filter-wrap">
                <button class="pf-filter-btn" id="pfFilterBtn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="6" x2="20" y2="6"/><line x1="8" y1="12" x2="16" y2="12"/><line x1="11" y1="18" x2="13" y2="18"/></svg>
                    Filter
                </button>
                <!-- Filter Dropdown -->
                <div class="pf-filter-dropdown" id="pfFilterDropdown">
                    <div class="pf-filter-col">
                        <div class="pf-filter-col-title">Deal Type:</div>
                        <label><input type="checkbox" value="traditional-search" data-filter="deal"> Traditional Search</label>
                        <label><input type="checkbox" value="self-funded" data-filter="deal"> Self Funded Search</label>
                        <label><input type="checkbox" value="long-term-hold" data-filter="deal"> Long Term Hold</label>
                        <label><input type="checkbox" value="independent-sponsor" data-filter="deal"> Independent Sponsor</label>
                    </div>
                    <div class="pf-filter-col">
                        <div class="pf-filter-col-title">Sector:</div>
                        <label><input type="checkbox" value="business-services" data-filter="sector"> Business Services</label>
                        <label><input type="checkbox" value="consumer-services" data-filter="sector"> Consumer Services</label>
                        <label><input type="checkbox" value="education" data-filter="sector"> Education</label>
                        <label><input type="checkbox" value="healthcare" data-filter="sector"> Healthcare</label>
                        <label><input type="checkbox" value="industrial" data-filter="sector"> Industrial Services</label>
                        <label><input type="checkbox" value="search-fund" data-filter="sector"> Search Fund</label>
                        <label><input type="checkbox" value="technology" data-filter="sector"> Technology</label>
                    </div>
                    <div class="pf-filter-col">
                        <div class="pf-filter-col-title">Year:</div>
                        <label><input type="checkbox" value="2024" data-filter="year"> 2024</label>
                        <label><input type="checkbox" value="2025" data-filter="year"> 2025</label>
                        <label><input type="checkbox" value="2026" data-filter="year"> 2026</label>
                    </div>
                    <div class="pf-filter-col">
                        <div class="pf-filter-col-title">Status:</div>
                        <label><input type="checkbox" value="current" data-filter="status"> Current</label>
                        <label><input type="checkbox" value="exited" data-filter="status"> Exited</label>
                    </div>
                </div>
            </div>
        </div>

        <!-- Active Filter Tags -->
        <div class="pf-active-filters" id="pfActiveTags"></div>

        <!-- Cards Grid -->
        <div class="pf-cards-grid" id="pfCardsGrid">

            <!-- Company 1: Nexus Retail Solutions -->
            <div class="pf-card" data-deal="traditional-search" data-sector="business-services" data-year="2024" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#1a6fc4;">NR<span>NEXUS RETAIL</span></div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Nexus Retail Solutions</h3>
                        <p>A leading B2B retail distribution and supply-chain management firm providing end-to-end logistics, inventory, and procurement services to mid-market retailers across South Asia.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector</em> Business Services</span>
                            <span><em>Location</em> Mumbai, India</span>
                            <span><em>Type</em> Traditional Search</span>
                            <span><em>Investment Date</em> 2024</span>
                            <span><em>Status</em> <span class="pf-badge current">Current</span></span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 2: Greenleaf Education Trust -->
            <div class="pf-card" data-deal="long-term-hold" data-sector="education" data-year="2024" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#3a7d44;">GL<span>GREENLEAF EDU</span></div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Greenleaf Education Trust</h3>
                        <p>A network of premium K&ndash;12 institutions and after-school learning centres focused on outcome-based, technology-integrated education across Tier-1 and Tier-2 cities.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector</em> Education</span>
                            <span><em>Location</em> Patna, India</span>
                            <span><em>Type</em> Long Term Hold</span>
                            <span><em>Investment Date</em> 2024</span>
                            <span><em>Status</em> <span class="pf-badge current">Current</span></span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 3: Meridian HealthCare -->
            <div class="pf-card" data-deal="self-funded" data-sector="healthcare" data-year="2024" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#c0392b;">MH<span>MERIDIAN HEALTH</span></div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Meridian HealthCare</h3>
                        <p>A multi-speciality diagnostic and outpatient care network delivering affordable, high-quality clinical services through 14 facilities integrating digital health records and telemedicine.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector</em> Healthcare</span>
                            <span><em>Location</em> Delhi NCR, India</span>
                            <span><em>Type</em> Self Funded Search</span>
                            <span><em>Investment Date</em> 2024</span>
                            <span><em>Status</em> <span class="pf-badge current">Current</span></span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 4: Ironclad Industrial -->
            <div class="pf-card" data-deal="independent-sponsor" data-sector="industrial" data-year="2025" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#5d4e37;">II<span>IRONCLAD GROUP</span></div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Ironclad Industrial Group</h3>
                        <p>A precision manufacturing and fabrication company supplying specialised components to automotive, aerospace, and heavy machinery clients across Jharkhand and Gujarat.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector</em> Industrial Services</span>
                            <span><em>Location</em> Jamshedpur, India</span>
                            <span><em>Type</em> Independent Sponsor</span>
                            <span><em>Investment Date</em> 2025</span>
                            <span><em>Status</em> <span class="pf-badge current">Current</span></span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 5: Vantage Digital Services -->
            <div class="pf-card" data-deal="traditional-search" data-sector="technology" data-year="2025" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#6a1fc2;">VD<span>VANTAGE DIGITAL</span></div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Vantage Digital Services</h3>
                        <p>A technology services and digital transformation partner helping enterprises modernise legacy systems, migrate to cloud, and deploy AI-powered process automation at scale.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector</em> Technology</span>
                            <span><em>Location</em> Bengaluru, India</span>
                            <span><em>Type</em> Traditional Search</span>
                            <span><em>Investment Date</em> 2025</span>
                            <span><em>Status</em> <span class="pf-badge current">Current</span></span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 6: Crest Consumer Brands -->
            <div class="pf-card" data-deal="self-funded" data-sector="consumer-services" data-year="2025" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#e67e22;">CB<span>CREST BRANDS</span></div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Crest Consumer Brands</h3>
                        <p>A direct-to-consumer FMCG company building a portfolio of purpose-led home, personal care, and food brands distributed through modern trade, e-commerce, and institutional channels.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector</em> Consumer Services</span>
                            <span><em>Location</em> Hyderabad, India</span>
                            <span><em>Type</em> Self Funded Search</span>
                            <span><em>Investment Date</em> 2025</span>
                            <span><em>Status</em> <span class="pf-badge current">Current</span></span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 7: Summit Search Partners -->
            <div class="pf-card" data-deal="traditional-search" data-sector="search-fund" data-year="2024" data-status="exited">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#2c3e50;">SS<span>SUMMIT SEARCH</span></div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Summit Search Partners</h3>
                        <p>A traditional search fund targeting the acquisition of a single established business in professional services across South and Southeast Asia — successfully exited after value realisation.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector</em> Search Fund</span>
                            <span><em>Location</em> Singapore</span>
                            <span><em>Type</em> Traditional Search</span>
                            <span><em>Investment Date</em> 2024</span>
                            <span><em>Status</em> <span class="pf-badge exited">Exited</span></span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 8: Clearpath Logistics -->
            <div class="pf-card" data-deal="long-term-hold" data-sector="industrial" data-year="2025" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#16a085;">CL<span>CLEARPATH</span></div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Clearpath Logistics</h3>
                        <p>A tech-enabled last-mile logistics and freight management company serving e-commerce, FMCG, and pharma clients with a proprietary route optimisation and fleet management platform.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector</em> Industrial Services</span>
                            <span><em>Location</em> Pune, India</span>
                            <span><em>Type</em> Long Term Hold</span>
                            <span><em>Investment Date</em> 2025</span>
                            <span><em>Status</em> <span class="pf-badge current">Current</span></span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Company 9: Pinnacle EdTech -->
            <div class="pf-card" data-deal="independent-sponsor" data-sector="education" data-year="2026" data-status="current">
                <div class="pf-card-inner">
                    <div class="pf-card-front">
                        <div class="pf-logo-placeholder" style="color:#8e44ad;">PE<span>PINNACLE EDTECH</span></div>
                    </div>
                    <div class="pf-card-back">
                        <h3>Pinnacle EdTech</h3>
                        <p>An online learning and upskilling platform for working professionals offering industry-aligned certification programmes in technology, management, and finance with top-tier university partners.</p>
                        <div class="pf-card-meta">
                            <span><em>Sector</em> Education</span>
                            <span><em>Location</em> Chennai, India</span>
                            <span><em>Type</em> Independent Sponsor</span>
                            <span><em>Investment Date</em> 2026</span>
                            <span><em>Status</em> <span class="pf-badge current">Current</span></span>
                        </div>
                    </div>
                </div>
            </div>

        </div><!-- /pf-cards-grid -->

        <!-- No Results -->
        <div class="pf-no-results" id="pfNoResults" style="display:none;">
            <p>No companies match your selected filters. Try clearing a filter.</p>
        </div>

    </div>
</section>

<style>
.section-portfolio-cards { padding: 100px 0; background: #F7F4F0; }
.pf-top-bar { display:flex; align-items:flex-start; justify-content:space-between; margin-bottom:40px; gap:24px; flex-wrap:wrap; }
.pf-title { font-family:'Outfit',sans-serif; font-size:clamp(1.9rem,3vw,2.8rem); font-weight:700; color:#111; margin-bottom:10px; line-height:1.15; }
.pf-subtitle { font-size:0.9rem; color:#888; max-width:340px; line-height:1.6; }
.pf-filter-wrap { position:relative; flex-shrink:0; }
.pf-filter-btn { display:inline-flex; align-items:center; gap:9px; padding:11px 24px; background:#2F1E13; color:#F1E8D9; border:none; border-radius:50px; font-family:'Outfit',sans-serif; font-size:0.88rem; font-weight:500; cursor:pointer; transition:all 0.25s ease; letter-spacing:0.03em; box-shadow:0 4px 16px rgba(47,30,19,0.18); }
.pf-filter-btn:hover, .pf-filter-btn.active { background:#C4A882; color:#1a1a1a; box-shadow:0 6px 24px rgba(196,168,130,0.3); }
.pf-filter-dropdown { position:absolute; top:calc(100% + 12px); right:0; background:#fff; border-radius:18px; box-shadow:0 24px 64px rgba(0,0,0,0.13); padding:28px 32px; display:none; gap:36px; z-index:200; min-width:580px; border:1px solid rgba(0,0,0,0.07); animation:pfDropIn 0.18s ease; flex-wrap:wrap; }
.pf-filter-dropdown.open { display:flex; }
@keyframes pfDropIn { from{opacity:0;transform:translateY(-8px)} to{opacity:1;transform:translateY(0)} }
.pf-filter-col { display:flex; flex-direction:column; gap:11px; min-width:130px; }
.pf-filter-col-title { font-family:'Outfit',sans-serif; font-size:0.7rem; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; color:#aaa; margin-bottom:2px; }
.pf-filter-col label { display:flex; align-items:center; gap:9px; font-size:0.85rem; color:#333; cursor:pointer; transition:color 0.18s; font-family:'Inter',sans-serif; }
.pf-filter-col label:hover { color:#2F1E13; }
.pf-filter-col input[type="checkbox"] { accent-color:#2F1E13; width:14px; height:14px; cursor:pointer; flex-shrink:0; }
.pf-active-filters { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:28px; min-height:8px; }
.pf-tag { display:inline-flex; align-items:center; gap:7px; padding:5px 14px; background:rgba(47,30,19,0.09); border-radius:50px; font-size:0.78rem; color:#2F1E13; font-family:'Outfit',sans-serif; font-weight:500; }
.pf-tag button { background:none; border:none; color:#2F1E13; cursor:pointer; font-size:1rem; line-height:1; padding:0; opacity:0.6; }
.pf-tag button:hover { opacity:1; }
.pf-cards-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:28px; }
@media(max-width:900px){.pf-cards-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:580px){.pf-cards-grid{grid-template-columns:1fr;} .pf-filter-dropdown{min-width:300px;right:-20px;}}
.pf-card { perspective:1100px; height:290px; }
.pf-card-inner { width:100%; height:100%; position:relative; transition:transform 0.7s cubic-bezier(0.4,0,0.2,1); transform-style:preserve-3d; }
.pf-card:hover .pf-card-inner { transform:rotateY(180deg); }
.pf-card-front, .pf-card-back { position:absolute; inset:0; border-radius:20px; backface-visibility:hidden; -webkit-backface-visibility:hidden; }
.pf-card-front { background:#fff; border:1px solid rgba(0,0,0,0.07); display:flex; align-items:center; justify-content:center; padding:32px; box-shadow:0 2px 16px rgba(0,0,0,0.05); transition:box-shadow 0.3s; }
.pf-card:hover .pf-card-front { box-shadow:0 16px 48px rgba(0,0,0,0.1); }
.pf-logo-placeholder { font-family:'Outfit',sans-serif; font-size:3rem; font-weight:700; letter-spacing:-0.02em; text-align:center; line-height:1; }
.pf-logo-placeholder span { font-size:0.28em; display:block; font-weight:400; letter-spacing:0.12em; margin-top:6px; color:#888; }
.pf-card-front img { max-width:72%; max-height:110px; object-fit:contain; }
.pf-card-back { background:linear-gradient(150deg,#2F1E13 0%,#4a2f1e 55%,#2F1E13 100%); transform:rotateY(180deg); padding:26px 28px; display:flex; flex-direction:column; justify-content:space-between; overflow:hidden; color:#F1E8D9; position:relative; }
.pf-card-back::after { content:''; position:absolute; bottom:-50px; right:-50px; width:180px; height:180px; border-radius:50%; background:rgba(196,168,130,0.07); pointer-events:none; }
.pf-card-back h3 { font-family:'Outfit',sans-serif; font-size:1.1rem; font-weight:600; color:#fff; margin-bottom:8px; }
.pf-card-back p { font-size:0.79rem; color:rgba(241,232,217,0.78); line-height:1.55; flex:1; overflow:hidden; display:-webkit-box; -webkit-line-clamp:4; -webkit-box-orient:vertical; }
.pf-card-meta { display:flex; flex-direction:column; gap:4px; margin-top:12px; border-top:1px solid rgba(196,168,130,0.2); padding-top:10px; }
.pf-card-meta span { font-size:0.74rem; color:rgba(241,232,217,0.65); display:flex; align-items:center; gap:6px; }
.pf-card-meta em { font-style:normal; color:#C4A882; font-weight:600; min-width:100px; }
.pf-badge { display:inline-block; padding:2px 9px; border-radius:50px; font-size:0.68rem; font-weight:700; letter-spacing:0.03em; }
.pf-badge.current { background:rgba(74,222,128,0.18); color:#86efac; }
.pf-badge.exited { background:rgba(251,146,60,0.18); color:#fdba74; }
.pf-card.pf-hidden { display:none; }
.pf-no-results { text-align:center; padding:80px 0; color:#999; font-size:1rem; }
</style>

<script>
(function(){
    var btn=document.getElementById('pfFilterBtn');
    var dropdown=document.getElementById('pfFilterDropdown');
    var grid=document.getElementById('pfCardsGrid');
    var noResults=document.getElementById('pfNoResults');
    var tagsWrap=document.getElementById('pfActiveTags');
    var checkboxes=dropdown?Array.from(dropdown.querySelectorAll('input[type="checkbox"]')):[];
    var labels={'traditional-search':'Traditional Search','self-funded':'Self Funded Search','long-term-hold':'Long Term Hold','independent-sponsor':'Independent Sponsor','business-services':'Business Services','consumer-services':'Consumer Services','education':'Education','healthcare':'Healthcare','industrial':'Industrial Services','search-fund':'Search Fund','technology':'Technology','current':'Current','exited':'Exited'};
    if(btn&&dropdown){
        btn.addEventListener('click',function(e){e.stopPropagation();dropdown.classList.toggle('open');btn.classList.toggle('active');});
        document.addEventListener('click',function(e){if(!dropdown.contains(e.target)&&e.target!==btn){dropdown.classList.remove('open');btn.classList.remove('active');}});
    }
    function applyFilters(){
        var active={};
        checkboxes.forEach(function(cb){if(cb.checked){var f=cb.dataset.filter;if(!active[f])active[f]=[];active[f].push(cb.value);}});
        tagsWrap.innerHTML='';
        Object.keys(active).forEach(function(fk){active[fk].forEach(function(val){var tag=document.createElement('div');tag.className='pf-tag';tag.innerHTML=(labels[val]||val)+' <button title="Remove">&times;</button>';tag.querySelector('button').addEventListener('click',function(){var cb=dropdown.querySelector('input[value="'+val+'"][data-filter="'+fk+'"]');if(cb){cb.checked=false;applyFilters();}});tagsWrap.appendChild(tag);});});
        var cards=grid.querySelectorAll('.pf-card');var visible=0;var noF=Object.keys(active).length===0;
        cards.forEach(function(card){
            if(noF){card.classList.remove('pf-hidden');visible++;return;}
            var show=true;
            Object.keys(active).forEach(function(fk){var attr=fk==='deal'?'deal':fk;var cardVal=card.dataset[attr];if(!active[fk].includes(cardVal))show=false;});
            if(show){card.classList.remove('pf-hidden');visible++;}else{card.classList.add('pf-hidden');}
        });
        noResults.style.display=visible===0?'block':'none';
    }
    checkboxes.forEach(function(cb){cb.addEventListener('change',applyFilters);});
})();
</script>

'''

new_content = content[:start_idx] + new_section + end_marker + content[end_idx + len(end_marker):]

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SUCCESS: portfolio.html updated!")
lines = new_content.count('\n')
print(f"Total lines: {lines}")
