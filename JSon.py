from socket import *
from threading import *
import random
import json

serverPort = 7




def handleClient(clientSocket, addr):
    ask = f'du har tre muligheder:\n 1. add \n 2. substract \n 3. random \n'

    clientSocket.send(ask.encode())

    while True:  
        
        sentence = clientSocket.recv(2048).decode()
       
       

        splitText = sentence.split()
        Text=''
        if(splitText[0].lower() == 'add'):
            talx = int (splitText[1])
            taly = int (splitText[2])

            dict = {
                f'tal1': talx, 'tal2': taly, 'Result': [talx + taly]
                
             }
             
            
            y = json.dumps(dict)
        
        elif (splitText[0].lower() == 'random'):
             talx = int (splitText[1])
             taly = int (splitText[2])
             dict = {
                f'tal1': talx, 'tal2': taly, 'Result' : [random.randint(talx, taly)]
             }
             y = json.dumps(dict)
       
        elif (splitText[0].lower() == 'substract'):
             talx = int (splitText[1])
             taly = int (splitText[2])
             dict = {
                f'tal1': talx, 'tal2': taly, 'Result': [talx - taly]
             }
        
             y = json.dumps(dict)


        else:
         dict = f'denne metode virker ikke {splitText[0]}'

         y = json.dumps(dict)

        clientSocket.send(y.encode())
    


serverSocket = socket (AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print('The server is ready to receive', serverSocket)


while True:
    connectionSocket, addr = serverSocket.accept()
    print('forbinder til en klient fra adressen', addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()