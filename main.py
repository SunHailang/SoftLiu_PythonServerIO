import math
import platform
import sys

import os, json
o_path = os.getcwd()
sys.path.append(o_path)

from Utils.DataBase.MySqlManager import MySqlManager
from SocketUtils.UDP_ServerManager import UDP_ServerManager
from SocketUtils.TCP_ServerManager import TCP_ServerManager
from SocketUtils.TCP_ClientManager import TCP_ClientManager
from Utils.AppConfigUtils import *

import threading, time

appConfig_path = 'Resources/AppConfig.json'

if __name__ == "__main__":
    print("Hello World !")
    initAppConfig(appConfig_path)
    platform = getPlatform()
    print('current platform: ' + platform)
    if platform == 'Linux_Ubuntu':
        ip, username, password, database = getMySqlConfig()
        # print(ip, username, password, database)
        
        sql = MySqlManager("10.192.91.40", "root", "hlsun123", "hlsun")
        data = sql.SelectData("select * from student where isDelete=1;")
        print(data[0], len(data))
        count = sql.GetCount("select count(*) from student;")
        print(count)

        # start client connection server
        client = TCP_ClientManager()
        clientThreat, clientSock = client.startThread()
        if clientSock:
            
            # start server
            tcp = TCP_ServerManager()
            serverThread = tcp.startThread()
            serverThread.join()

    elif platform == 'Windows':
        pass
    elif platform == 'iMac':
        tcp = TCP_ServerManager()
        startThread = tcp.startThread()
        startThread.join()

    
    # udp = UDP_ServerManager()
    # tcp = TCP_ServerManager()
    # startThread = tcp.startThread()
    '''
    while True:
        city = input('input: ')
        if city == 'quit':
            break
        else:
            print("I'd love to go to " + city.title() + "!")
    '''
    
    
    print('end')
