import math
import platform
import sys
from Utils.DataBase.MySqlManager import MySqlManager
from SocketUtils.UDP_ServerManager import UDP_ServerManager
from SocketUtils.TCP_ServerManager import TCP_ServerManager

import threading, time

print("Hello World .")


if __name__ == "__main__":
    print("Hello World !")
    sql = MySqlManager("localhost", "root", "hlsun123", "hlsun")
    data = sql.SelectData("select * from student where isDelete=1;")
    print(data[0], len(data))
    count = sql.GetCount("select count(*) from student;")
    print(count)

    # udp = UDP_ServerManager()
    tcp = TCP_ServerManager()

    while True:
        city = input()
        if city == 'quit':
            break
        else:
            print("I'd love to go to " + city.title() + "!")
    print('end')
