
# coding: utf-8

# In[ ]:

from socket import *
serverport = 12000;
serverSocket = socket(AF_INET, SOCK_STREAM);
serverSocket.bind(('', serverport));
serverSocket.listen(1);
print('The server is ready to receive');
while(1):
    connectionSocket, addr = serverSocket.accept();
    sentence = connectionSocket.recv(1024);
    print(sentence)
    CapitalizedSentence = sentence.decode().upper();
    connectionSocket.send(CapitalizedSentence.encode());
    connectionSocket.close();


# In[ ]:



