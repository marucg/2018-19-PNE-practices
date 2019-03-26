'''Program for making an html file with the echo
of the received message from the user '''
import http.server
import socketserver
import termcolor

PORT = 8087


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        # PRINTING THE REQUEST LINE
        termcolor.cprint(self.requestline, 'green')

        message = self.path[10:]
        print('this is message', message)
        if self.path == '/':
            with open('form2-ex.html', 'r') as r:
                contents = r.read()
        elif message:
            if '&chk=on' in message:
                message = message.upper()[:-7]
            contents = """<html>
            <body style="background-color: yellow;">
            <title>Echo of the received message</title>         
            <h1>Echo of the received message:</h1>
            <br>""" + message + """<br><br>
            <a href="http://localhost:8087/">Main Page</a>
            </body>
            </html>"""
        else:
            with open('error-ex-2.html', 'r') as r:
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
