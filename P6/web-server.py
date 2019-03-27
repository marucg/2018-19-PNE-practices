"""Program that reads the operations requested and generates
    a result in a html file"""
import http.server
import socketserver
import termcolor
from Seq import Seq


PORT = 8088


class TestHandler(http.server.BaseHTTPRequestHandler):

# CREATING FUNCTIONS FOR OPERATION AND VALIDATION OF THE SEQUENCE
    def functions(self, seq, operation, str_seq):
        counter = seq.count(str_seq)
        if operation == 'countA':
            return counter.get('A')
        elif operation == 'countC':
            return counter.get('C')
        elif operation == 'countT':
            return counter.get('T')
        elif operation == 'countG':
            return counter.get('G')
        elif operation == 'percA':
            return seq.perc('A', str_seq)
        elif operation == 'percC':
            return seq.perc('C', str_seq)
        elif operation == 'percT':
            return seq.perc('T', str_seq)
        elif operation == 'percG':
            return seq.perc('G', str_seq)

    def validation(self, sequence_dna):
        dna_bases = 'ACTG'
        for word in sequence_dna:
            if word not in dna_bases:
                return True
        return False


    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

    # DIVIDING THE MESSAGE BY THE OPTIONS THE USER ENTERED
        divide_msg = self.path.split('&')
    # MAIN MESSAGE
        sequence = divide_msg[0][14:].upper()
        if self.path == '/' or self.path == '/seq':
            with open('main_page.html', 'r') as r:
                contents = r.read()
        elif sequence:
    # TWO OPTIONS THAT CAN EXIST DEPENDING ON THE SEQUENCE INTRODUCED
        # WHEN THE SEQUENCE HAS INVALID BASES
            if self.validation(sequence):
                response = 'You have introduced an invalid sequence'
                contents = """<html>
                <body style="background-color: yellow;">
                <title>Echo of the received message</title>         
                <h1>Echo of the received message:</h1>
                <p><h3>Error: </h3>""" + response + """</p>
                </body>
                </html>"""
        # THE SEQUENCE IS VALID
            else:
                s1 = Seq(sequence)
                contents = """<html>
                <body style="background-color: yellow;">
                <title>Echo of the received message</title>         
                <h1>Echo of the received message:</h1>
                <p><h3>Sequence of DNA: </h3>""" + sequence + """</p>
                </body>
                </html>"""
        # ADDING THE LENGTH IF IT IS REQUESTED
                if '&chk=on' in self.path:
                    length = s1.len()
                    contents = contents + "<p><h3>Length: </h3>" + str(length) + "</p>"
        # OBTAINING THE OPERATIONS REQUESTED
                sequence = sequence
                base = self.path.split('base=')[1].split("&")[0]
                operation = self.path.split('operation=')[1].split("&")[0]
                contents = contents + "<p><h3>Operation: </h3>" + operation + "</p>" + "<p><h3>Base: </h3>" + base + "</p>"
                request = operation + base
        # MAKING THE OPERATIONS
                resolve = self.functions(s1, request, sequence)
                contents = contents + "<p><h3>Solution: </h3>" + str(resolve) + "</p>"
    # WHEN THE RESOURCE IS NOT VALID
        else:
            with open('error.html', 'r') as r:
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
