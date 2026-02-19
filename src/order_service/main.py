from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)

        if parsed_path.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, HealthCheckHandler)
    print(f'Starting server on port {port}...')
    print(f'Health check endpoint: http://localhost:{port}/health')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
