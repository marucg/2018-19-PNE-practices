import socket
from termcolor import colored

# SERVER IP, PORT
IP = "10.0.2.15"
PORT = 8087

# WAIT UNTIL I HAVE ALL THE DATA LIKE AN INPUT TO CONNECT TO THE SERVER
option = True
while option:
    # The client is blocking the server....  NOT A GOOD DESIGN!!!
    #--------PUT THE INPUT FIRST--------

    msg = input("Please enter a message (to exit write 'EXIT'): ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: ", response)

    final_message = colored('-PROGRAM FINISHED-', 'red')

    if response == final_message:
        s.close()
        break

    else:
        s.close()






