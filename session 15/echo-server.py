import http.server
import socketserver
import termcolor

PORT = 8080


class TestHandler(http.server.BaseHTTPRequestHandler):
    # CREATING OBJECTS
    # THE FUNCTION HAS TO BE CALLED 'do_GET'
    def do_GET(self):

        # PRINTING THE REQUEST LINE
        termcolor.cprint(self.requestline, 'green')

        f = open('form1.html', 'r')
        contents = f.read()
        print('this is the message', contents)

    # GENERATING THE RESPONSE MESSAGE
        self.send_response(200)
    # SENDING THE HEADER (specifying the type of text)
        self.send_header('Content Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
    # SENDING THE BODY
        self.wfile.write(str.encode(contents))

        message = self.path[10:]
        if self.path != '/':
            file == 'error.html'
        else:
            file ==
# ------MAIN PROGRAM------
# PUTTING THE IP AS '' MEANS THAT WILL DEFAULT IP OF THE COMPUTER

with socketserver.TCPServer(('', PORT), TestHandler) as httpd:
    print('Serving at PORT', PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


print('Sever stopped')
