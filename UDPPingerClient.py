__author__ = 'Fernando'
from socket import *
from time import time

numOfRequest = 10
timeout_secs = 1
lostPackets = 0

# Socket variables
serverName = 'localhost'
serverPort = 12000

# Open UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(timeout_secs)  # Set timeout in secs

for packet in range(numOfRequest):
    currentTime = time() * 1000
    message = "Ping " + str(packet + 1) + " of " + str(numOfRequest) + " received"
    try:
        clientSocket.sendto(message, (serverName, serverPort))  # send message to server
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # Receive modified message from server
        print modifiedMessage + " Round-Trip-Time: " + str(time() * 1000 - currentTime)
    except timeout:  # if timed out from above
        print("Ping " + str(packet + 1) + " timed out")
        lostPackets += 1
        continue  # Continue sending packets if timed out
clientSocket.close()
print
print("Connection Closed!")
print
print("Number of Lost Packets: " + str(lostPackets))
