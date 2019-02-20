import socket
from termcolor import colored

PORT = 8087
IP = '10.0.2.15'
max_open_request = 1
# if a sixth user wants to connect it will be rejected


def process_client(msg,cs):
    # READING THE MESSAGE FROM THE CLIENT
    msg_color = colored(msg, 'yellow')
    print('Message from the client: ',msg_color )

    # SENDING THE MESSAGE BACK TO THE CLIENT
    cs.send(str.encode(msg_color))

def finished_program(msg,cs):
    final_message = colored('-PROGRAM FINISHED-', 'red')
    cs.send(str.encode(final_message))
    cs.close()

# creating a socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

# listening the client
serversocket.listen(max_open_request)

print('Socket ready!', serversocket)
# print('Socket ready! {}'.format(serversocket))


while True:
    print('Waiting for connections at', IP, PORT)
    # print('Waiting for connections at {},{}'.format(IP,PORT)

    (clientsocket, address) = serversocket.accept()

    # -PROCESS- the client request
    print('Attending client', address)

    msg = clientsocket.recv(2000).decode('utf-8')

    if msg != 'EXIT':
        process_client(msg, clientsocket)
    else:
        finished_program(msg, clientsocket)
        break





