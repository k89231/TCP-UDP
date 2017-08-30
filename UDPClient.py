
# coding: utf-8

# In[ ]:

from socket import *
servername = 'IP/hostname'   # Set the host name for the server
serverport = 12000;      	 # Set the port number for the server

clientSocket = socket(AF_INET, SOCK_DGRAM)                          # Set the socket for client. SOCK_DGRAM stands fot UDP rather than TCP
																	# AF_INET stands for IPV4
                                                                    # The port number of the client will be set by system automatically
    
message = input('Input lower case sentence');                       # String to send.
clientSocket.sendto(message.encode(), (servername, serverport));
modifiedMessage, serverAddress = clientSocket.recvfrom(2048);       # The length of cache equals 2048.
                                                                    # serverAddress includes the IP of the server and the port number of the 
                                                                    # server socket.
print(modifiedMessage.decode())
clientSocket.close();


# In[ ]:




# In[ ]:



