import socket

# SERVER IP, PORT
IP = "212.128.253.96"
PORT = 8082

# WAIT UNTIL I HAVE ALL THE DATA LIKE AN INPUT TO CONNECT TO THE SERVER
while True:
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

    s.close()

    # Print the server's response
    print("Response: {}".format(response))

