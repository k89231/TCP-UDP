
# coding: utf-8

# In[ ]:

from socket import *
serverPort = 12000;
serverSocket = socket(AF_INET, SOCK_DGRAM);
serverSocket.bind(('', serverPort));
print('The server is about to receive')
while(True):
    message, clientAddress = serverSocket.recvfrom(2048);
    modifiedMessage = message.upper();
    serverSocket.sendto(modifiedMessage, clientAddress);


# In[ ]:

serverSocket.close()


# In[ ]:



