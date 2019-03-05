# IT WILL OPEN MY PAGE 'MARU'S PAGE'
import http.server
import socketserver

PORT = 8007
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

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Content-length', len(str.encode(index)))
            self.end_headers()
            self.wfile.write(str.encode(index))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.send_header('Content-length', len(str.encode(error)))
            self.end_headers()
            self.wfile.write(str.encode(error))


        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print('Serving at port', PORT)

    httpd.serve_forever()