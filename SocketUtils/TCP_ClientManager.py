'''
    __author__ = Sun Hai Lang
    __date__ = 2019-09-23
'''

import sys

import os, json
o_path = os.getcwd()
sys.path.append(o_path)

import socket, json, struct, math
from socket import error as SocketError
import errno

import threading
from MyThread import MyThread
from Utils.AppConfigUtils import *

from SocketUtils.TCP_CommandUtil import TCP_CommandUtil

class TCP_ClientManager(object):

    def __init__(self):
        self.platform = getPlatform()
        host, ip, port = getTcpConfig()
        self.TCP_IP_ADDRESS = socket.gethostbyname(host)
        self.TCP_PORT_NO = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.TCP_IP_ADDRESS, self.TCP_PORT_NO)
        self.sock.connect(self.server_address)
        

    def startThread(self):
        #thread.Thread(target=self.recvData).start()
        thread1 = MyThread().createThread(self.recvTCP)
        thread1.start()
        # thread2 = 
        return thread1
    
    def recvData(self, args={}):
        try:
            while True:
                try:
                    cacheBuff = None
                    datasize = bytes[1024]
                except error:
                    print(error)
                    break
        finally:
            if self.sock:
                self.sock.close()
        

    def __del__(self):
        pass

if __name__ == "__main__":
    recvData = bin(40)
    print(recvData)