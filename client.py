import base64, ssl
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.aol.com', 465)

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_TLSv1)
clientSocket.connect(mailserver)
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
    
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')
  
# Start TLS  
# clientSocket.send('250-STARTTLS'.encode())    
# recv_tls = clientSocket.recv(1024).decode()
# print(recv)
# if recv_tls[:3] != '220':
#     print('220 reply not received from server.')


# Authentication
username = 'christiandaga@aol.com'
password = 'lgjxzjcothoxuhkd'
encoded = ('\x00'+username+'\x00'+password).encode()
encoded = base64.b64encode(encoded)
clientSocket.send('AUTH PLAIN '.encode()+encoded+'\r\n'.encode())
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

# Send MAIL FROM command and print server response.
# Fill in start
clientSocket.send(('MAIL FROM:'+username+'\r\n').encode())
recv2 = clientSocket.recv(1024).decode()
print('MAIL FROM recieved: '+recv2)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
clientSocket.send(('RCPT TO:'+username+'\r\n').encode())
recv3 = clientSocket.recv(1024).decode()
print('RCPT TO recieved: '+recv3)
# Fill in end

# Send DATA command and print server response.
# Fill in start
clientSocket.send(('DATA\r\n').encode())
recv4 = clientSocket.recv(1024).decode()
print('DATA recieved: '+recv4)
# Fill in end

# Send message data.
# Fill in start
clientSocket.send('Subject: Test\r\n'.encode())
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print('MSG recieved: '+recv5)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send(('QUIT\r\n').encode())
recv6 = clientSocket.recv(1024).decode()
print('QUIT received: '+recv6)
# Fill in end

clientSocket.close()