from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        #message = "Hello, World!"
        self.wfile.write(bytes("Duje Popovic, 31.5.2021, Port je 8000", "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()