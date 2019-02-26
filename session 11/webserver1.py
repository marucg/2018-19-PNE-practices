import socket
import termcolor



# Change this IP to yours!!!!!
IP = "212.128.253.84"
PORT = 8082
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    # -- I ADD THESE LINES --
    # THE CONTENT IS IN HTML ------ you can change the color in light'' or put the color only
    with open('Index.html', 'r') as r:
        content = r.read()

    # THE 200 MEANS THAT EVERYTHING IS OK
    status_line = 'HTTP/1.1 200 ok\r\n'

    header = 'Content-Type: text/html\r\n'
    # I HAVE TO PUR THE LINE AT THE END CAREFUL!!!!!!!!!!!!!!!!!!!!!!!!!!
    header += 'Content-Length: ' + str(len(str.encode(content))) + '\r\n'

    response_msg = status_line + header + '\r\n' + content
    print(content)
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
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)

# IN THE WEB COPY THE IP AND PORT LIKE --IP:PORT-- the (:) are necessary
# I have 10 messages and i only execute it once
# (it means that the server if searching for an answer but is not getting a response so it stops)
# IF I WANT TO RECEIVE THE MESSAGE FROM THE TEACHER I USE THE IP AND PORT OF THE TEACHER





