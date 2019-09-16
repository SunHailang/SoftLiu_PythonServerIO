import math
import platform
import sys

import os, json
o_path = os.getcwd()
sys.path.append(o_path)

from Utils.DataBase.MySqlManager import MySqlManager
from SocketUtils.UDP_ServerManager import UDP_ServerManager
from SocketUtils.TCP_ServerManager import TCP_ServerManager
from Utils.AppConfigUtils import *

import threading, time

print("Hello World .")

appConfig_path = 'Resources/AppConfig.json'

if __name__ == "__main__":
    print("Hello World !")
    initAppConfig(appConfig_path)
    ip, username, password, database = getMySqlConfig()
    # print(ip, username, password, database)
    
    sql = MySqlManager("10.192.91.40", "root", "hlsun123", "hlsun")
    data = sql.SelectData("select * from student where isDelete=1;")
    print(data[0], len(data))
    count = sql.GetCount("select count(*) from student;")
    print(count)



    '''
    # udp = UDP_ServerManager()
    tcp = TCP_ServerManager()
    startThread = tcp.startThread()
    
    while True:
        city = input('input: ')
        if city == 'quit':
            break
        else:
            print("I'd love to go to " + city.title() + "!")
    startThread.join()
    '''
    print('end')
