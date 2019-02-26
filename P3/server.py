'''Program that calculates the requests from the client'''
import socket
from termcolor import colored
from Seq import Seq

PORT = 8085
IP = '10.0.2.15'
open_requests = 1

# FUNCTION THAT RETURNS EVERY CALCULATION
def total_functions(seq, operation, str_seq):
    counter = seq.count(str_seq)
    if operation == 'len':
        return seq.len()
    elif operation == 'complement':
        return seq.complement()
    elif operation == 'reverse':
        return seq.reverse()
    elif operation == 'countA':
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
    elif operation =='percG':
        return seq.perc('G', str_seq)

# FUNCTION THAT WILL PROCESS THE REQUESTS FROM THE CLIENT
# If the message is an empty string respond with -alive-
# Check if the sequence received contains the bases -A,C,T,G-
# If it is true respond with -ok- and send the calculations
def client(message, cs):
    if message == '\n':
        response = 'ALIVE'
    else:
        message = message.split('\n')
        sequence = message[0].upper()
        for word in sequence:
            if word != 'A' and word != 'C' and word != 'G' and word != 'T':
                response = '-ERROR-\n'
            else:
                response = 'OK\n'

                object_seq = Seq(sequence)
                str_seq = sequence
                for request in range(1, len(message) -1):
                    resolve = total_functions(object_seq, message[request], str_seq)
                    response = response + str(resolve) + '\n'

    # Sending the calculations
    cs.send(str.encode(response))

    cs.close()

#Creating a socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(open_requests)

while True:
    print('Waiting for connections at', IP, PORT)

    (clientsocket, address) = serversocket.accept()

    # -PROCESS- the client request
    print('Attending client', address)

    message = clientsocket.recv(2048).decode('utf-8')
    first_word = message.split('\n')
    first_word = first_word[0]

    # CHECKING IF THE CLIENT WAN TO END THE PROGRAM
    if first_word != 'exit':
        client(message, clientsocket)
    else:
        end = colored('-PROGRAM FINISHED-', 'red')
        clientsocket.send(str.encode(end))
        clientsocket.close()
        break
