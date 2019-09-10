'''
    author: Sun Hai Lang
    create time: 2019-09-02
'''

import socket, json
import threading
from MyThread import MyThread

from SocketUtils.TCP_CommandUtil import TCP_CommandUtil


class TCP_ServerManager(object):

    def __init__(self):
        self.TCP_IP_ADDRESS = "192.168.218.128"
        # self.TCP_IP_ADDRESS = "202.59.232.58"
        self.TCP_PORT_NO = 11060
        self.clientList = []
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        print('ip:', socket.gethostbyname(self.host))
        # Bind the socket to the port
        self.server_address = (self.TCP_IP_ADDRESS, self.TCP_PORT_NO)
        print('address:',self.server_address)
        self.sock.bind(self.server_address)
        # Listen for incoming connections
        self.sock.listen(10)
        

    def startThread(self):
        #thread.Thread(target=self.recvData).start()
        thread1 = MyThread(1, 'udp-thread',1).createThread(self.startTCP)
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
                MyThread(2, 'udp-thread',2).createThread(self.recvData, args={'con':connection, 'client':client_address}).start()
            finally:
                break
            
    def recvData(self, args={}):
        connection = args['con']
        client = args['client']
        try:    
            print('connection from', client)        
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                request = data.decode('utf-8')
                print('received "%s"' % request)
                if request:
                    if request == 'exit':
                        break
                    else:
                        commandJson = json.loads(request)
                        command = TCP_CommandUtil(commandJson)
                        resultCode = command.getResult()
                        result_send = json.dumps(resultCode)
                        print('sending data back to the client : ' + result_send)
                        result = result_send.encode('utf-8')                        
                        connection.sendall(result)
                else:
                    print('no more data from.')
                    break
        finally:
            # Clean up the connection
            if self.clientList.index(client) >= 0:
                self.clientList.remove(client)
            if connection:
                connection.close()


        