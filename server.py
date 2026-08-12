import http.server
import socketserver
import os

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code == 404:
            # If the file is not found, serve the custom 404.html page instead
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            # Try to read and serve the 404.html file
            try:
                with open('404.html', 'rb') as file:
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.wfile.write(b"404 Not Found - Custom 404.html file is missing!")
        else:
            super().send_error(code, message, explain)

# Set up and start the server
with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    print("Serving custom 404.html for broken links...")
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
