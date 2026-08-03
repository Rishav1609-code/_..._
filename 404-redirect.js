/*
 * 404 Redirect Handler for vXr Holdings
 * Intercepts clicks on internal links and redirects to 404.html if the page doesn't exist.
 * Works on localhost, Live Server, and any static file server.
 */
(function () {
    // List of valid pages on the site
    var validPages = [
        'index.html',
        'services.html',
        'about.html',
        'investment-criteria.html',
        'portfolio.html',
        'contact.html',
        'terms-of-use.html',
        'privacy-policy.html',
        '404.html'
    ];

    document.addEventListener('click', function (e) {
        var link = e.target.closest('a');
        if (!link) return;

        var href = link.getAttribute('href');
        if (!href) return;

        // Skip external links, anchors, mailto, tel, javascript
        if (href.startsWith('http') || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:') || href.startsWith('javascript:')) return;

        // Extract just the filename (ignore query strings and hashes)
        var page = href.split('?')[0].split('#')[0];

        // If it's a valid page, let it through
        if (validPages.indexOf(page) !== -1) return;

        // Otherwise, redirect to 404
        e.preventDefault();
        window.location.href = '404.html';
    });
})();
