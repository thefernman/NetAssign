__author__ = 'Fernando'

from socket import *
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

recipient = "<fcamp001@fiu.edu>"
sender = "<familytreetesting@gmail.com>"
username = "familytreetesting@gmail.com"
password = '___'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'  # Fill in start #Fill in end
serverPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverPort))
recv = clientSocket.recv(1024)
print("recv: " + recv)
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print("recv1: " + recv1)
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Request an encrypted connection
ttlCommand = "STARTTLS\r\n"
clientSocket.send(ttlCommand)
tls_recv = clientSocket.recv(1024)
print tls_recv
if tls_recv[:3] != '220':
    print '220 reply not received from server'

# Encrypt the socket
ssl_clientSocket = ssl.wrap_socket(clientSocket)

# Send the AUTH LOGIN command and print server response.
authCommand = 'AUTH LOGIN\r\n'
ssl_clientSocket.write(authCommand)
auth_recv = ssl_clientSocket.read(1024)
print auth_recv
if auth_recv[:3] != '334':
    print '334 reply not received from server'

# Send username and print server response.
uname = base64.b64encode(username) + '\r\n'
ssl_clientSocket.write(uname)
uname_recv = ssl_clientSocket.read(1024)
print uname_recv
if uname_recv[:3] != '334':
    print '334 reply not received from server'

# Send password and print server response.
pword = base64.b64encode(password) + '\r\n'
ssl_clientSocket.write(pword)
pword_recv = ssl_clientSocket.read(1024)
print pword_recv
if pword_recv[:3] != '235':
    print '235 reply not received from server'

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: ' + sender + '\r\n'
ssl_clientSocket.write(mailFromCommand)
recv2 = ssl_clientSocket.read(1024)
print("recv2: " + recv2)
if recv2[:3] != '250':
    print '250 reply not received from server.'
# Fill in end

# Send RCPT TO command and print server response.
sendToCommand = 'RCPT TO: ' + recipient + '\r\n'
ssl_clientSocket.write(sendToCommand)
recv3 = ssl_clientSocket.read(1024)
print("recv3: " + recv3)
if recv3[:3] != '250':
    print '250 reply not received from server.'

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
ssl_clientSocket.write(dataCommand)
recv4 = ssl_clientSocket.read(1024)
print("recv4: " + recv4)
if recv4[:3] != '354':
    print '354 reply not received from server.'

# Send message data.
ssl_clientSocket.write(msg)

# Message ends with a single period.
ssl_clientSocket.write(endmsg)
recv5 = ssl_clientSocket.read(1024)
print("recv5: " + recv5)
if recv5[:3] != '250':
    print '250 reply not received from server.'

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
ssl_clientSocket.write(quitCommand)
recv6 = ssl_clientSocket.read(1024)
print recv6
if recv6[:3] != '221':
    print '221 reply not received from server.'

'''
some notes:
after ssl, recv() become read() and send() become write()
so
clientSocket.send(heloCommand) -> ssl_clientSocket.write(quitCommand)
recv1 = clientSocket.recv(1024) -> recv6 = ssl_clientSocket.read(1024)

something is wrong with the socket module and ssl.wrap_socket

'''