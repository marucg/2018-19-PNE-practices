# RECEIVING THE SEQUENCE FROM THE CLIENT AND SENDING THE COMPLEMENTARY SEQUENCE
import socket
# CREATING CLASS SEQ


class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def complement(self):
        dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        seq = ''
        for base in self.strbases:
            if base == 'A':
                seq += dictionary.get('A')
            elif base == 'C':
                seq += dictionary.get('C')
            elif base == 'T':
                seq += dictionary.get('T')
            else:
                seq += dictionary.get('G')
        return seq


PORT = 8084
IP = '10.0.2.15'
max_open_request = 1


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(max_open_request)

print('Socket ready!', serversocket)
print('Waiting for connections at', IP, PORT)

(clientsocket, address) = serversocket.accept()

print('Attending client', address)
# OBTAINING THE SEQUENCE FROM THE CLIENT
msg = clientsocket.recv(2000).decode('utf-8')
# CREATING SEQ OBJECT
print(msg)
msg_seq = Seq(msg)
# TRANSFORMING THE SEQUENCE INTO THE COMPLEMENTARY
final_msg = msg_seq.complement()
# SENDING THE THE FINAL SEQUENCE TO THE CLIENT
clientsocket.send(str.encode(final_msg))
clientsocket.close()




