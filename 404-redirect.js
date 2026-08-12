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

    // === ON-LOAD CHECK ===
    // Catch invalid URLs typed directly into the address bar 
    // (Works if the server acts as an SPA and serves a default HTML page for missing routes)
    var currentPath = window.location.pathname.split('/');
    var currentFile = currentPath.pop();
    if (!currentFile) currentFile = 'index.html';

    // If the current URL is NOT in the valid pages list, redirect to 404.html
    if (validPages.indexOf(currentFile) === -1 && (currentFile.endsWith('.html') || currentFile.indexOf('.') === -1)) {
        window.location.replace('404.html');
    }

    document.addEventListener('click', function (e) {
        var link = e.target.closest('a');
        if (!link || !link.href) return;

        var url;
        try {
            // Use the fully resolved URL6
            url = new URL(link.href);
        } catch (err) {
            return;
        }

        // Ignore mailto, tel, javascript, etc.
        if (url.protocol !== 'http:' && url.protocol !== 'https:' && url.protocol !== 'file:') return;

        // Only intercept clicks to the same origin (for web servers).
        // For local files (file://), origin is often "null", so we skip the origin check.
        if (url.protocol !== 'file:' && url.origin !== window.location.origin) return;

        // Skip same-page anchors
        if (url.pathname === window.location.pathname && url.hash) return;

        // Extract filename from the path 
        var pathSegments = url.pathname.split('/');
        var filename = pathSegments.pop();

        // If no filename (e.g., linked to root '/'), default to index.html
        if (!filename) filename = 'index.html';

        // Allow valid pages
        if (validPages.indexOf(filename) !== -1) return;

        // Otherwise, redirect to 404
        e.preventDefault();
        window.location.href = '404.html';
    });
})();
