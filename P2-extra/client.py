# ASKING THE USER OF THE SEQUENCE AND SENDING IT TO THE SERVER
# OBTAINING THE COMPLEMENT OF THE SEQUENCE INTRODUCED

import socket

PORT = 8084
IP = '10.0.2.15'

user = input('Please enter a sequence: ').upper()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# CONNECTING TO THE SERVER
s.connect((IP, PORT))
# SENDING THE SEQUENCE
s.send(str.encode(user))
# RECEIVING THE COMPLEMENTARY SEQUENCE
response = s.recv(2048).decode()
print('Response: ', response)
print('\n-PROGRAM FINISHED-')
s.close()