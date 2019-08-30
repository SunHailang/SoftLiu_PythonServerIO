
from socket import *
import threading as thread
import time

class UDP_Manager(object):

    def __init__(self):

        self.serverPort = 8888
        self.serverSocket = socket(AF_INET, SOCK_DGRAM)
        self.serverSocket.bind(('',self.serverPort))
        print('Waiting for connection...')

        thread.Thread(target=self.recvData).start()

        

    def recvData(self):
        while True:
            message, clientAddress = self.serverSocket.recvfrom(2048)
            print('Receive Message: %s' %message.decode('utf-8'))
            modifiedMessage = message.decode('utf-8').upper()
            self.serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)

    
    def __del__(self):
        pass