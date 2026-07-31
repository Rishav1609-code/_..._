import os
import re

html_file = r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\contact.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Define the old section to replace
# We want to replace from <!-- ===== SUB HERO ===== --> down to the end of <section class="section-contact"... </section>
pattern = r"<!-- ===== SUB HERO ===== -->[\s\S]*?</section>\s*</div>\s*<!-- ===== FOOTER ===== -->"

new_layout = """<!-- ===== NEW CONTACT LAYOUT ===== -->
        <section class="section-contact-split" style="padding: 120px 40px; background: #ffffff; min-height: 100vh; display: flex; align-items: center; max-width: 1600px; margin: 0 auto;">
            <div class="contact-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; width: 100%; height: calc(100vh - 160px); min-height: 700px;">
                
                <!-- Left Image Poster -->
                <div class="contact-poster" style="position: relative; border-radius: 32px; overflow: hidden; height: 100%;">
                    <!-- Handshake image -->
                    <img src="images/handshake.png" alt="Handshake" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(0.7);" onerror="this.src='images/about-image.png'" />
                    
                    <!-- Overlay Text -->
                    <div style="position: absolute; top: 60px; left: 60px; z-index: 2;">
                        <h1 style="color: #ffffff; font-size: clamp(3rem, 5vw, 4.5rem); font-weight: 500; letter-spacing: -0.02em; margin: 0;">Get in Touch</h1>
                    </div>

                    <!-- Glass Info Card -->
                    <div style="position: absolute; bottom: 40px; left: 40px; background: rgba(20,20,20,0.6); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 32px 40px; display: flex; flex-direction: column; gap: 24px; z-index: 2;">
                        <a href="mailto:info@vxrholdings.com" style="display: flex; align-items: center; gap: 16px; color: #ffffff; text-decoration: none; font-size: 1.1rem; font-weight: 500;">
                            <div style="width: 48px; height: 48px; border-radius: 50%; background: #ffffff; display: flex; align-items: center; justify-content: center; color: #1a1a1a;">
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                            </div>
                            info@vxrholdings.com
                        </a>
                        <div style="display: flex; align-items: center; gap: 16px; color: #ffffff; font-size: 1.1rem; font-weight: 500;">
                            <div style="width: 48px; height: 48px; border-radius: 50%; background: #ffffff; display: flex; align-items: center; justify-content: center; color: #1a1a1a;">
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            </div>
                            Bihar, INDIA
                        </div>
                    </div>
                </div>
                
                <!-- Right Form Container -->
                <div class="contact-form-container" style="background: #FAFAFA; border-radius: 32px; padding: 60px; height: 100%; display: flex; flex-direction: column; justify-content: center;">
                    <form id="contactForm" class="contact-form" style="display: flex; flex-direction: column; gap: 40px; height: 100%; justify-content: space-between;">
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
                            <div style="display: flex; flex-direction: column; gap: 16px;">
                                <label for="name" style="font-weight: 500; color: #333; font-size: 1rem;">Name</label>
                                <input type="text" id="name" required placeholder="Enter name" style="padding-bottom: 12px; border: none; border-bottom: 1px solid #ddd; font-family: inherit; font-size: 1.1rem; outline: none; background: transparent; transition: border-color 0.3s; color: #111;"/>
                            </div>
                            <div style="display: flex; flex-direction: column; gap: 16px;">
                                <label for="email" style="font-weight: 500; color: #333; font-size: 1rem;">Email</label>
                                <input type="email" id="email" required placeholder="Enter email" style="padding-bottom: 12px; border: none; border-bottom: 1px solid #ddd; font-family: inherit; font-size: 1.1rem; outline: none; background: transparent; transition: border-color 0.3s; color: #111;"/>
                            </div>
                        </div>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
                            <div style="display: flex; flex-direction: column; gap: 16px;">
                                <label for="phone" style="font-weight: 500; color: #333; font-size: 1rem;">Phone</label>
                                <input type="tel" id="phone" placeholder="Enter phone" style="padding-bottom: 12px; border: none; border-bottom: 1px solid #ddd; font-family: inherit; font-size: 1.1rem; outline: none; background: transparent; transition: border-color 0.3s; color: #111;"/>
                            </div>
                            <div style="display: flex; flex-direction: column; gap: 16px;">
                                <label for="company" style="font-weight: 500; color: #333; font-size: 1rem;">Company Name</label>
                                <input type="text" id="company" placeholder="Enter company name" style="padding-bottom: 12px; border: none; border-bottom: 1px solid #ddd; font-family: inherit; font-size: 1.1rem; outline: none; background: transparent; transition: border-color 0.3s; color: #111;"/>
                            </div>
                        </div>
                        
                        <div style="display: flex; flex-direction: column; gap: 16px;">
                            <label for="message" style="font-weight: 500; color: #333; font-size: 1rem;">Message</label>
                            <textarea id="message" required placeholder="Enter message" rows="2" style="padding-bottom: 12px; border: none; border-bottom: 1px solid #ddd; font-family: inherit; font-size: 1.1rem; outline: none; background: transparent; resize: vertical; color: #111;"></textarea>
                        </div>
                        
                        <div style="display: flex; align-items: center; margin-top: 10px;">
                            <div style="border: 1px solid #ddd; border-radius: 4px; padding: 12px 16px; background: #fff; display: flex; align-items: center; gap: 12px; width: max-content;">
                                <input type="checkbox" id="recaptcha" style="width: 24px; height: 24px; cursor: pointer;">
                                <label for="recaptcha" style="font-size: 0.95rem; cursor: pointer; color: #333;">I'm not a robot</label>
                                <img src="https://www.gstatic.com/recaptcha/api2/logo_48.png" style="width: 32px; margin-left: 20px; opacity: 0.8;" alt="reCAPTCHA">
                            </div>
                        </div>

                        <div>
                            <button type="submit" class="btn btn-primary" style="background: #757575; border-radius: 50px; padding: 16px 32px; border: none; display: inline-flex; width: auto; font-size: 1.05rem; font-weight: 500;">
                                <span>Send a message</span>
                                <span class="icon-arrow-dynamic" style="margin-left: 12px;">
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
                                </span>
                            </button>
                        </div>
                    </form>
                </div>
            </div>
            <style>
                input:focus, textarea:focus {
                    border-bottom-color: #333 !important;
                }
                .btn-primary:hover {
                    background: #5c5c5c !important;
                }
                @media (max-width: 1024px) {
                    .contact-grid {
                        grid-template-columns: 1fr !important;
                        height: auto !important;
                    }
                    .contact-poster {
                        height: 500px !important;
                    }
                    .contact-form-container {
                        padding: 40px !important;
                    }
                }
                @media (max-width: 767px) {
                    .contact-form > div[style*="display: grid"] {
                        grid-template-columns: 1fr !important;
                        gap: 24px !important;
                    }
                }
            </style>
        </section>
    </div>
    <!-- ===== FOOTER ===== -->"""

new_content = re.sub(pattern, new_layout, content)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Contact layout updated.")
