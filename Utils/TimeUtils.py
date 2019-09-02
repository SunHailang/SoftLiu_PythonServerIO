'''
    author: Sun Hai Lang 
    create time: 2019-09-02

'''

# time.strftime 默认为当前的时间

import time, math
import json

# return 时间戳 和 本地时间(yyyy-MM-dd HH:mm:ss)
def GetCurrentTime():
    ticks = math.floor(time.time())
    localTime = time.strftime('%Y-%m-%d %H:%M:%S')
    return ticks, localTime

    