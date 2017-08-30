
# coding: utf-8

# In[3]:

from socket import *
servername = 'hostname/IP';
serverport = 12000;

clientsocket = socket(AF_INET, SOCK_STREAM);          # SOCK_STREAM stands for TCP protocol, AF_INET stands for IPV4
clientsocket.connect((servername, serverport));
sentence = input('Input sentence with lowercase : ');

sentence = sentence.encode();
clientsocket.send(sentence);
modifiedsentence = clientsocket.recv(1024).decode();           # Length of cache
print('From Server : ' + modifiedsentence);

clientsocket.close()


# In[ ]:



