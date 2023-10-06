from socket import *
from threading import *
import random

serverPort = 7




def handleClient(clientSocket, addr):
    ask = f'choose an option:\n 1. add \n 2. substract \n 3. random \n'
    clientSocket.send(ask.encode())
    while True:  
        
        sentence = clientSocket.recv(2048).decode()
        if not sentence:
            break
       

        splitText = sentence.split()
        Text=''
        if(splitText[0].lower() == 'add'):
            talx = int (splitText[1])
            taly = int (splitText[2])
            Text = f'{talx} + {taly} = {(talx+taly)}\n\n' 
        
        elif (splitText[0].lower() == 'random'):
             talx = int (splitText[1])
             taly = int (splitText[2])
             Text = f' {(random.randint(talx,taly))}\n\n'
       
        elif (splitText[0].lower() == 'substract'):
             talx = int (splitText[1])
             taly = int (splitText[2])
             Text = f'{talx} - {taly} = {(talx-taly)}\n\n' 


        else:
            Text = f'denne metode er ikke mulig {splitText[0]}'

        clientSocket.send(Text.encode())
    


serverSocket = socket (AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print('The server is ready to receive', serverSocket)


while True:
    connectionSocket, addr = serverSocket.accept()
    print('forbinder til en klient fra adressen', addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()
    