
import socket
import threading as thread
import time
from MyThread import MyThread

class UDP_ServerManager(object):

    

    def __init__(self):
        self.UDP_IP_ADDRESS = "127.0.0.1"
        self.UDP_PORT_NO = 8888
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSocket.bind((self.UDP_IP_ADDRESS, self.UDP_PORT_NO))
        print('Waiting for connection...')

        #thread.Thread(target=self.recvData).start()
        MyThread(1, 'udp-thread',1).createThread(self.recvData).start()
        

    def recvData(self, args={}):
        while True:
            message, clientAddress = self.serverSocket.recvfrom(2048)
            print('Receive Message: %s' %message.decode('utf-8'))
            messageData = message.decode('utf-8')
            self.sendtoData(clientAddress, messageData)

    def sendtoData(self, clientAddress, messageData):
        self.serverSocket.sendto(messageData.encode('utf-8'), clientAddress)

    
    def __del__(self):
        pass