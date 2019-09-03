import json
import math
import sys
import time

import socket

# import imp
# TimeUtils = imp.load_source('TimeUtils','../SoftLiu_PythonServerIO/Utils/TimeUtils.py')

from MyThread import MyThread


server = socket.socket()
server.bind(('127.0.0.1', 11060))
server.listen(2)

index_content = '''
HTTP/1.x 200 ok
Content-Type: text/html
<html>
    <head>
    </head>
    <body>
        <p>{}</p>
    </body>                         
</html> 
'''


if __name__ == "__main__":
    print("Hello World.")

    print(socket.gethostname())

    '''
    ticks, localTime = TimeUtils.GetCurrentTime()
    print(ticks,localTime)
    
    print(math.floor(time.time()))
    print(time.localtime(math.floor(time.time())))
    
    x = {
        "ticks": ticks,
        "localTime": time.strftime('%Y-%m-%d %H:%M:%S'),
        "status": 0
    }

    du = json.dumps(x)
    print(du)
    lo = json.loads(du)
    print(lo)
    '''

    '''
    while True:
        conn, addr = server.accept()
        
        request = conn.recv(1024).decode('utf-8')
        print(addr, request)
        if not request: continue
        # method = request.split(' ')[0]
        # locate = request.split(' ')[1]
        #if method == 'GET':
        print('execute sync script')
        conn.sendall(time.strftime('%Y-%m-%d %H:%M:%S').encode('utf-8'))
        conn.close()
    '''
