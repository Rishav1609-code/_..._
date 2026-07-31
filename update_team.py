import os
import re

file_path = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\about.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the new team members HTML
new_team_html = """                <div class="team-grid">
                    <!-- Member 1 -->
                    <div class="team-card reveal">
                        <div class="team-top">
                            <div class="team-photo">
                                <div style="width:100%;height:100%;background:linear-gradient(135deg, #C4A882, #8B6E4E);display:flex;align-items:center;justify-content:center;color:white;font-family:'Outfit',sans-serif;font-size:2.4rem;font-weight:300;">VR</div>
                            </div>
                            <div class="team-info">
                                <div class="team-name-flex">
                                    <h3>Vishu Raj</h3>
                                    <div class="team-role">Founder &amp; Chairman</div>
                                </div>
                                <blockquote class="team-quote">Setting the visionary direction and ensuring our long-term strategic alignment with global markets.</blockquote>
                                <a href="#" class="team-linkedin" target="_blank">LinkedIn</a>
                            </div>
                        </div>
                        <div class="team-bottom">
                            <ul class="team-points">
                                <li>Pioneered the core vision and foundational strategy of vXr Holdings.</li>
                                <li>Extensive experience in macro-economic positioning and capital allocation.</li>
                            </ul>
                        </div>
                    </div>
                    
                    <!-- Member 2 -->
                    <div class="team-card reveal reveal-delay-1">
                        <div class="team-top">
                            <div class="team-photo">
                                <div style="width:100%;height:100%;background:linear-gradient(135deg, #5B7FA6, #3D5A80);display:flex;align-items:center;justify-content:center;color:white;font-family:'Outfit',sans-serif;font-size:2.4rem;font-weight:300;">RR</div>
                            </div>
                            <div class="team-info">
                                <div class="team-name-flex">
                                    <h3>Rishav Raj</h3>
                                    <div class="team-role">Founder &amp; CEO</div>
                                </div>
                                <blockquote class="team-quote">Driving transformative growth through strategic execution and operational excellence.</blockquote>
                                <a href="#" class="team-linkedin" target="_blank">LinkedIn</a>
                            </div>
                        </div>
                        <div class="team-bottom">
                            <ul class="team-points">
                                <li>Spearheading daily operations and driving the company's ambitious growth targets.</li>
                                <li>Proven track record of scaling enterprises from inception to maturity.</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Member 3 -->
                    <div class="team-card reveal">
                        <div class="team-top">
                            <div class="team-photo">
                                <div style="width:100%;height:100%;background:linear-gradient(135deg, #8C9970, #5B6B3F);display:flex;align-items:center;justify-content:center;color:white;font-family:'Outfit',sans-serif;font-size:2.4rem;font-weight:300;">AS</div>
                            </div>
                            <div class="team-info">
                                <div class="team-name-flex">
                                    <h3>Adesh Shrivastava</h3>
                                    <div class="team-role">Co-Founder &amp; MD</div>
                                </div>
                                <blockquote class="team-quote">Fostering robust partnerships and overseeing our diverse investment portfolio.</blockquote>
                                <a href="#" class="team-linkedin" target="_blank">LinkedIn</a>
                            </div>
                        </div>
                        <div class="team-bottom">
                            <ul class="team-points">
                                <li>Managing critical stakeholder relationships and leading deal structuring.</li>
                                <li>Deep expertise in private equity and structured finance.</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Member 4 -->
                    <div class="team-card reveal reveal-delay-1">
                        <div class="team-top">
                            <div class="team-photo">
                                <div style="width:100%;height:100%;background:linear-gradient(135deg, #A882C4, #6E4E8B);display:flex;align-items:center;justify-content:center;color:white;font-family:'Outfit',sans-serif;font-size:2.4rem;font-weight:300;">DD</div>
                            </div>
                            <div class="team-info">
                                <div class="team-name-flex">
                                    <h3>Dipti Divya</h3>
                                    <div class="team-role">Co-Founder &amp; CTO</div>
                                </div>
                                <blockquote class="team-quote">Leveraging cutting-edge technology to create seamless, scalable infrastructure.</blockquote>
                                <a href="#" class="team-linkedin" target="_blank">LinkedIn</a>
                            </div>
                        </div>
                        <div class="team-bottom">
                            <ul class="team-points">
                                <li>Leading the technological roadmap and digital transformation initiatives.</li>
                                <li>Specializes in building robust platforms for high-growth tech ventures.</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Member 5 -->
                    <div class="team-card reveal">
                        <div class="team-top">
                            <div class="team-photo">
                                <div style="width:100%;height:100%;background:linear-gradient(135deg, #C48282, #8B4E4E);display:flex;align-items:center;justify-content:center;color:white;font-family:'Outfit',sans-serif;font-size:2.4rem;font-weight:300;">SS</div>
                            </div>
                            <div class="team-info">
                                <div class="team-name-flex">
                                    <h3>Sakshi Shreya</h3>
                                    <div class="team-role">Co-Founder &amp; CGO</div>
                                </div>
                                <blockquote class="team-quote">Accelerating market presence and driving sustainable revenue generation.</blockquote>
                                <a href="#" class="team-linkedin" target="_blank">LinkedIn</a>
                            </div>
                        </div>
                        <div class="team-bottom">
                            <ul class="team-points">
                                <li>Directing go-to-market strategies and global expansion efforts.</li>
                                <li>Expert in market analytics, brand positioning, and scaling revenue operations.</li>
                            </ul>
                        </div>
                    </div>
                </div>"""

# Regex to replace the entire team-grid block
pattern = r'<div class="team-grid">[\s\S]*?</div>\s*</div>\s*</section>'
replacement = new_team_html + '\n            </div>\n        </section>'

new_content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Team section updated successfully!")
