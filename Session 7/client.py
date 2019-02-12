# Programming our first client (ALWAYS EXPLAIN WHAT I'M DOING IN THE FILE)

import socket

# CREATE A SOCKET FOR COMMUNICATING WITH THE SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# We will always use these parameters
print('Socket created')

PORT = 8080
IP = '212.128.253.64'

# Connecting to the server
s.connect((IP,PORT))
print('The end')

# Sending messages (i cannot write string i have to transform it binary)
s.send(str.encode('HELLO FROM MY CLIENT'))
#Receving in bits and converting it
msg = s.recv(2048).decode('utf-8')
print('MESSAGE FROM THE SERVER')
print(msg)
s.close()