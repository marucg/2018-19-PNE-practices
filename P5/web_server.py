'''Creating a program for accessing to several pages
    using a http module'''

import http.server
import socketserver

PORT = 8006


# CREATING AND OBJECT  -HANDLER-
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('Get received')
        print('Request Line:' + self.requestline)
        print(' cmd: ' + self.command)
        print(' path: ' + self.path)
    # OPTIONS THAT THE USER COULD ENTER
        if self.path == '/':
            file = 'index.html'
        elif self.path == '/pink':
            file = 'pink.html'
        elif self.path == '/blue':
            file = 'blue.html'
        else:
            file = 'error.html'
    # OPEN THE FILE
        with open(file, 'r') as r:
            content = r.read()
    # HTTP MODULE
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-length', len(str.encode(content)))
        self.end_headers()
        self.wfile.write(str.encode(content))
        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print('Serving at port', PORT)

    httpd.serve_forever()
