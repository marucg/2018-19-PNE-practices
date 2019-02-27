"""Web server that will give access to three different pages.
    These pages will be in Html form"""

import socket
import termcolor


IP = "10.0.2.15"
PORT = 8080
requests = 1


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    msg = cs.recv(2048).decode("utf-8")

    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

# OBTAINING THE REQUEST
    msg_divided = msg.split(' ')
    user = msg_divided[1]
    user_request = user.replace("/", '')

#CHECKING WHAT HAS REQUESTED THE USER
    if user_request == '':
        file = 'index.html'
    elif user_request == 'blue':
        file = 'blue.html'
    elif user_request == 'pink':
        file = 'pink.html'
    else:
        file = 'error.html'

# OPEN THE FILE REQUESTED
    with open(file, 'r') as r:
        content = r.read()

    status_line = 'HTTP/1.1 200 ok\r\n'
    header = 'Content-Type: text/html\r\n'
    header += 'Content-Length: ' + str(len(str.encode(content))) + '\r\n'

    response_msg = status_line + header + '\r\n' + content
    cs.send(str.encode(response_msg))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(requests)

print("Socket ready: {}".format(serversocket))

while True:
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)