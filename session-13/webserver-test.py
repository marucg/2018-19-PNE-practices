# IT WILL OPEN MY PAGE 'MARU'S PAGE'
import http.server
import socketserver

PORT = 8002
# Its call whenever there is a request


# CREATING AND OBJECT  -HANDLER-
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('Get received')
    # SEPARATING THE MESSAGES
        print('Request Line:' + self.requestline)
        print(' cmd: ' + self.command)
        print(' path: ' + self.path)

        content = 'I am the happy server! :-)'

    # THE FIRST LINE
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print('Serving at port', PORT)

    httpd.serve_forever()
# CALLING OUR OWN HANDLER

# WHEN I RUN IT AFTER THE / IT SPECIFIES THE RESOURCE
# IT MEANS THAT IN WEB SERVER I CANT PUT 'LOCALHOST:PORT/HOLA' THE HOLA WILL BE THE RESORUCE

# IN THE WEB SERVER IN THE TOP RIGHT CLICK IN 'WEB DEVELOPER'
# THEN CLICK IN 'NETWORK' AND RELOAD THE PAGE
# CLICK IN THE LINES AND CHECK EVERYTHING (SOME TYPE Of debug)