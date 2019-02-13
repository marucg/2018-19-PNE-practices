# Creating the client and importing the class from class_client

from class_client import Seq
import socket

PORT = 8088
IP = '212.128.253.64'

option = True
while option:
    user = input('Please enter a sequence: ').upper()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s1 = Seq(user)
    s2 = s1.reverse()
    s2_converted = Seq(s2)
    s3 = s2_converted.complement()
    s.send(str.encode(s3))
    s.close()