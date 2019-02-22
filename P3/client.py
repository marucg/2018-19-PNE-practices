'''Program that will process the requests of the user'''
import socket
from termcolor import colored

PORT = 8085
IP = '10.0.2.15'

while True:
    # EXPLAINING THE PROGRAM TO THE USER
    print('Operations: len, complement, reverse, count(base) and perc(base).')
    print('To finish the program write "exit".')
    message = ''
    request = input("Please introduce the sequence and the operations you want to obtain: ")

    # SENDING THE MESSAGES WITH THE \n
    while len(request) > 0:
        message = message + request + "\n"
        request = str(input(""))

    # WHEN THE MESSAGE IS AN EMPTY STRING
    if len(message) == 0:
        message = "\n"

    # CREATING SOCKET
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((IP, PORT))

    s.send(str.encode(message))

    response = s.recv(2048).decode()

    print(response)

    final_message = colored('-PROGRAM FINISHED-', 'red')

    # CHECKING IF THE USER WANTS TO END THE PROGRAM
    if response == final_message:
        s.close()
        break

    else:
        s.close()
