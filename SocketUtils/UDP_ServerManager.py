
import socket
import threading as thread
import time
from MyThread import MyThread
from Utils.AppConfigUtils import *

class UDP_ServerManager(object):

    

    def __init__(self):
        ip, port = getUdpConfig()
        self.UDP_IP_ADDRESS = ip
        self.UDP_PORT_NO = port
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSocket.bind((self.UDP_IP_ADDRESS, self.UDP_PORT_NO))
        print('Waiting for connection...')

        #thread.Thread(target=self.recvData).start()
        MyThread().createThread(self.recvData).start()
        

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