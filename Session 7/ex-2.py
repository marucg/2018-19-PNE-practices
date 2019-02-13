import socket

PORT = 8085
IP = '212.128.253.64'
option = True

while option:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    user = input('Please enter a phrase: ')
    print(user)
    s.send(str.encode(user))
    s.close()

