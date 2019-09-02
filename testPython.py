import json
import math
import sys
import time

import imp
TimeUtils = imp.load_source('TimeUtils','../SoftLiu_PythonServerIO/Utils/TimeUtils.py')

from MyThread import MyThread



if __name__ == "__main__":
    
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