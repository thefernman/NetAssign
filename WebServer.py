# import socket module
from socket import * 
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
# Fill in start
serverPort = 12000
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()  # Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024)  # Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        output_data = f.read()  # Fill in start #Fill in end

        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')

        # Send the content of the requested file to the client
        for i in range(0, len(output_data)):
            connectionSocket.send(output_data[i])
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')

        # Close client socket
        serverSocket.close()