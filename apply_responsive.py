import re
import sys

with open(r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\styles.css", "r", encoding="utf-8") as f:
    content = f.read()

# Find the start of the @media (max-width: 1024px) block
# I will use a regex to split the file before the first `@media (max-width: 1024px)`
match = re.search(r"@media\s*\(\s*max-width:\s*1024px\s*\)", content)

if not match:
    print("Could not find @media (max-width: 1024px)")
    sys.exit(1)

base_css = content[:match.start()]

responsive_css = """
/* ==========================================================================
   RESPONSIVE OVERHAUL (MOBILE-FIRST GRACEFUL DEGRADATION)
   ========================================================================== */

@media (max-width: 1024px) {
    :root {
        --page-gap-top: 28px;
        --page-gap-side: 28px;
    }
    .container {
        padding: 0 var(--page-gap-side);
    }
    
    /* Hero Adjustments */
    .hero-content {
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 120px 20px 40px;
        gap: 30px;
    }
    .hero-text-block-glass-split, .hero-text-block-glass {
        max-width: 100%;
        text-align: center;
        padding: 30px 20px;
    }
    .hero-text-block-glass-split .hero-title, .hero-text-block-glass .hero-title {
        font-size: clamp(2.5rem, 5vw, 3.5rem);
    }
    .hero-stat-block {
        align-items: center;
        width: 100%;
    }
    .hero-stat-card {
        width: 100%;
        min-width: unset;
        text-align: center;
    }
    .hero-stat-value {
        justify-content: center;
    }
    .hero-btn-flex {
        justify-content: center;
    }

    /* Grids & Flex containers */
    .family-wrap, .section-header, .methodology-grid, .team-top {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .section-header-left {
        margin-bottom: 24px;
        flex: unset;
    }
    .key-cards, .team-grid {
        grid-template-columns: 1fr;
    }
    .footer-grid, .metrics-grid, .pf-cards-grid, .ecosystem-bento {
        grid-template-columns: repeat(2, 1fr) !important;
    }
    
    /* Services */
    .service-row, .service-row.reverse {
        flex-direction: column;
        gap: 30px;
        margin-bottom: 60px;
    }
    .service-img-wrapper {
        width: 100%;
        flex: none;
        max-height: 400px;
    }
}

@media (max-width: 768px) {
    :root {
        --page-gap-top: 20px;
        --page-gap-side: 20px;
    }
    
    /* Navbar */
    .navbar-links, .nav-cta {
        display: none;
    }
    .mobile-menu-toggle {
        display: flex;
    }
    .mobile-menu {
        display: block;
    }

    /* Typography */
    h1 { font-size: clamp(2rem, 7vw, 2.5rem); }
    h2 { font-size: clamp(1.8rem, 6vw, 2.2rem); }
    
    /* Force smaller paddings on all major sections */
    .section-hero { min-height: 100vh; }
    .section-sub-hero { min-height: 100vh; }
    .section-family, .section-methodology, .section-portfolio, .section-team, .section-cta, .section-key, .section-service-showcase {
        padding: 60px 0 !important;
    }
    
    /* Collapse grids to 1 column */
    .metrics-grid, .footer-grid, .pf-cards-grid, .contact-grid, .ecosystem-bento {
        grid-template-columns: 1fr !important;
        gap: 20px;
    }
    
    .portfolio-card {
        flex: unset;
        width: 100%;
    }

    /* Miscellaneous Fixes */
    .family-left {
        min-height: 300px;
    }
    .footer-bottom {
        flex-direction: column;
        text-align: center;
        gap: 16px;
    }
    .footer-socials {
        justify-content: center;
        padding-top: 20px;
    }
    .team-photo {
        max-width: 100%;
        height: auto;
        aspect-ratio: 1/1;
    }
    .service-content h2 {
        font-size: 2rem;
    }
}

@media (max-width: 480px) {
    .hero-btn-flex {
        flex-direction: column;
        width: 100%;
        gap: 15px;
    }
    .hero-btn-flex .btn {
        width: 100%;
        justify-content: center;
    }
    .hero-stat-value {
        font-size: 3rem;
    }
}

@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}
"""

with open(r"c:\--\vXr_DEMO\LANDING PAGE\xVr_LANDING_PAGE\styles.css", "w", encoding="utf-8") as f:
    f.write(base_css + responsive_css)

print("styles.css responsive overhaul applied.")
