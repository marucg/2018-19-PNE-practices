'''file opening the index or error html
    depending on the path introduced'''
import http.server
import socketserver

PORT = 8005
# Its call whenever there is a request


# CREATING AND OBJECT  -HANDLER-
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        with open('index.html', 'r') as i:
            index = i.read()
        with open('error.html', 'r') as p:
            error = p.read()
        print('Get received')
    # SEPARATING THE MESSAGES
        print('Request Line:' + self.requestline)
        print(' cmd: ' + self.command)
        print(' path: ' + self.path)
    # OPTIONS
        if self.path == '/':
            file = 'index.html'
        else:
            file = 'error.html'

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