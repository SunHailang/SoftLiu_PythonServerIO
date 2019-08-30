import math
import platform
import sys
from Utils.DataBase.MySqlManager import MySqlManager
from SocketUtils.UDP_Manager import UDP_Manager

import threading, time
from socket import *

print("Hello World .")


if __name__ == "__main__":
    print("Hello World !")
    sql = MySqlManager("localhost", "root", "hlsun123", "hlsun")
    data = sql.SelectData("select * from student where isDelete=1;")
    print(data[0], len(data))
    count = sql.GetCount("select count(*) from student;")
    print(count)

    udp = UDP_Manager()

    while True:
        time.sleep(1)
        print("runing...")
