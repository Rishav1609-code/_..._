import http.server
import socketserver
import os

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code == 404:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Serve the custom 404.html page
            try:
                with open('404.html', 'rb') as f:
                    self.wfile.write(f.read())
            except FileNotFoundError:
                super().send_error(code, message, explain)
        else:
            super().send_error(code, message, explain)

Handler = CustomHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Custom 404 page is ENABLED.")
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
