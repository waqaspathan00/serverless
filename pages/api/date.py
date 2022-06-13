from http.server import BaseHTTPRequestHandler
from datetime import datetime


class handler(BaseHTTPRequestHandler):
    """ this route does NOT work, but it should trigger at localhost:3000/api/date"""

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
        return
