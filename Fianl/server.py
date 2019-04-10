import http.server
import socketserver
import termcolor

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        termcolor.cprint(self.requestline, 'yellow')

    # DIVIDING THE MESSAGE BY THE OPTIONS THE USER ENTERED
        divide_msg = self.path.split('&')
    # MAIN MESSAGE
        sequence = divide_msg[0][14:].upper()
        if self.path == '/' or self.path == '/seq':
            with open('Index.html', 'r') as r:
                contents = r.read()

    # GENERATING THE RESPONSE MESSAGE
        self.send_response(200)
    # SENDING THE HEADER (specifying the type of text)
        self.send_header('Content Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
    # SENDING THE BODY
        self.wfile.write(str.encode(contents))


# ------MAIN PROGRAM------
with socketserver.TCPServer(('', PORT), TestHandler) as httpd:
    print('Serving at PORT', PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


print('Sever stopped')
