'''
    author: Sun Hai Lang
    create time: 2019-09-02
'''

import socket
import threading
import MyThread

class TCP_ServerManager(object):

    def __init__(self):
        self.TCP_IP_ADDRESS = "127.0.0.1"
        self.TCP_PORT_NO = 11060
        self.clientList = []
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        # Bind the socket to the port
        self.server_address = (self.host, self.TCP_PORT_NO)
        self.sock.bind(self.server_address)
        # Listen for incoming connections
        self.sock.listen(10)
        #thread.Thread(target=self.recvData).start()
        MyThread.MyThread(1, 'udp-thread',1).createThread(self.startTCP).start()

    def startTCP(self, args={}):
        # Wait for a connection
        print('waiting for a connection...')
        while True:
            connection, client_address = self.sock.accept()
            self.clientList.append(client_address)
            MyThread.MyThread(2, 'udp-thread',2).createThread(self.recvData, args={'con':connection, 'client':client_address}).start()
            
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
                if data:
                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print('no more data from', client)
                    break
               
        finally:
            # Clean up the connection
            if self.clientList.index(client) >= 0:
                self.clientList.remove(client)
            connection.close()


        