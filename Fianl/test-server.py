import http.client
import json
import http.server
import socketserver
import termcolor



PORT = 8001
METHOD = 'GET'
ENDPOINT = '/info/species?content-type=application/json'
HOSTNAME = 'rest.ensembl.org'


headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
r1 = conn.getresponse()
print()
data = r1.read().decode("utf-8")
conn.close()

# ----------------------------------
def species():
    information = json.loads(data)
    species_info = information['species']
    for element in species_info:
        name = element['display_name']
        print(name)

#name_sp = species()

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        termcolor.cprint(self.requestline, 'yellow')


        endpoints = ['/']
        if self.path == '/' or self.path == '/seq':
            with open('Index.html', 'r') as r:
                contents = r.read()
        print('this is sequence', self.path)

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

