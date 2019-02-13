import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8091
IP = '212.128.253.78'

# Connecting to the server
s.connect((IP,PORT))

s.send(str.encode('De mi para mi'))
#Receving in bits and converting it
msg = s.recv(2048).decode('utf-8')
print('Message from the server')
print(msg)
s.close()