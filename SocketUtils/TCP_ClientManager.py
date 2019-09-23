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
        try:
            self.TCP_IP_ADDRESS = socket.gethostbyname(host)
            self.TCP_PORT_NO = port
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_address = (self.TCP_IP_ADDRESS, self.TCP_PORT_NO)
            self.sock.connect(self.server_address)
        except SocketError as e:
            self.sock = None
            print(e.errno)
        
        

    def startThread(self):
        if self.sock:
            #thread.Thread(target=self.recvData).start()
            thread1 = MyThread().createThread(self.recvData)
            thread1.start()
            return thread1, self.sock
        else:
            return None, None
        
    
    def recvData(self, args={}):
        try:
            recv_buffer = 1024
            recv_size = 0
            recevied_data = b''  #客户端每次发来内容的计数器
            while True:
                try:
                    data = connection.recv(recv_buffer)
                    recvLen, = struct.unpack('i', data)
                    print('recv data length: {}'.format(recvLen))
                    
                    while True:
                        try:
                            data = connection.recv(recv_buffer)
                            recv_size = recv_size + len(data)
                            recevied_data += data
                            if recv_size >= recvLen:
                                # deal with 
                                request = recevied_data.decode('utf-8')
                                print(request)

                                recv_size = 0
                                recevied_data = b''
                                break
                        except SocketError as e:
                            recv_size = 0
                            recevied_data = b''
                            print(e.errno)
                            break                        
                except SocketError as e:
                    print(e.errno)
                    break
        finally:
            if self.sock:
                self.sock.close()
        

    def __del__(self):
        pass

if __name__ == "__main__":
    recvData = bin(40)
    print(recvData)