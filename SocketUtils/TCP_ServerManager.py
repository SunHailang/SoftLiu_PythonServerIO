'''
    author: Sun Hai Lang
    create time: 2019-09-02
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


class TCP_ServerManager(object):

    def __init__(self):
        host, ip, port = getTcpConfig()
        self.TCP_IP_ADDRESS = socket.gethostbyname(host)
        # self.TCP_IP_ADDRESS = "202.59.232.58"
        self.TCP_PORT_NO = port
        self.clientList = []
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.host = socket.gethostname()
        # print('ip:', socket.gethostbyname(self.host))
        # Bind the socket to the port
        self.server_address = (self.TCP_IP_ADDRESS, self.TCP_PORT_NO)
        print('address:',self.server_address)
        self.sock.bind(self.server_address)
        # Listen for incoming connections
        self.sock.listen(10)
        
    def __del__(self):
        print('TCP Socket Close.')
        if self.sock:
            self.sock.close()

    def startThread(self):
        #thread.Thread(target=self.recvData).start()
        thread1 = MyThread().createThread(self.startTCP)
        thread1.start()
        # thread2 = 
        return thread1
        

    def startTCP(self, args={}):
        # Wait for a connection
        print('waiting for a connection...')
        while True:
            try:
                connection, client_address = self.sock.accept()
                self.clientList.append(client_address)
                MyThread().createThread(self.recvData, args={'con':connection, 'client':client_address}).start()
            except:
                print('server closed.')
                break
            
    def recvData(self, args={}):
        connection = args['con']
        client = args['client']
        try:    
            print('connection from', client)
            # Receive the data in small chunks and retransmit it
            while True:
                try:
                    data = connection.recv(1024)
                    request = data.decode('utf-8')
                    print('received "%s"' % request)
                    '''
                    if request:
                        if request == 'exit':
                            break
                        else:
                            commandJson = json.loads(request)
                            command = TCP_CommandUtil(commandJson)
                            resultCode = command.getResult()
                            self.sendData(connection, resultCode)
                    else:
                        print('no more data from.')
                        break
                    '''
                    connection.close()
                except SocketError as e:
                    print(e.errno)
                    break                
                
        finally:
            # Clean up the connection
            if self.clientList.index(client) >= 0:
                self.clientList.remove(client)
            print('close connection.', connection)
            if connection:
                connection.close()
            

    def sendData(self, conn, result):
        result_header = struct.pack('i', result['size'])
        conn.sendall(result_header)
        data = result['result']
        conn.sendall(data)

if __name__ == "__main__":
    hostname = '79864185.ngrok.io'
    # ip = socket.gethostbyname(host)
    # print(host)
    ipname = socket.gethostbyname(hostname)
    print('host : {} , ip : {}'.format(hostname, ipname))
    