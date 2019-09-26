'''
    author: Sun Hai Lang 
    create time: 2019-09-02

'''

# time.strftime 默认为当前的时间

import time, math
import json
import datetime

import calendar

import operator

import os


class UTC(datetime.tzinfo):
    def __init__(self, offset = 0):
        self._offset = offset

    def utcoffset(self, dt):
        return datetime.timedelta(hours=self._offset)
    
    def tzname(self, dt):
        return 'UTC +%s' % self._offset
    
    def dst(self, dt):
        return datetime.timedelta(hours=self._offset)

# return 时间戳 和 本地时间(yyyy-MM-dd HH:mm:ss)
def GetLocalTime():
    ticks = math.floor(time.time())
    localTime = time.strftime('%Y-%m-%d %H:%M:%S')
    return ticks, localTime

def GetUtcTime():
    ticks = math.floor(datetime.datetime.utcnow().timestamp())
    utcTime = datetime.datetime.fromtimestamp(ticks)
    return ticks, utcTime
    
def timestampTodatetime(stamp):
    localTicks = datetime.datetime.fromtimestamp(stamp)
    utcTicks = datetime.datetime.utcfromtimestamp(stamp)
    return localTicks, utcTicks

def getYearOfDay(dt):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totalday = 0
    if calendar.isleap(dt.year):
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month in range(1, dt.month):
        totalday  = totalday + days[month-1]
    totalday = totalday + dt.day
    return totalday


if __name__ == "__main__":
    print('date.max:', datetime.date.max)
    print('date.min:', datetime.date.min)
    print('date.today():', datetime.date.today())
    print('date.fromtimestamp():', datetime.date.fromtimestamp(time.time()))

    utcnow = datetime.datetime.utcnow()
    
    print('utc time: ', datetime.datetime.utcnow())
    print('local time: ',datetime.datetime.now().timestamp())
    #北京时间
    beijing = datetime.datetime(utcnow.year, utcnow.month, utcnow.day, utcnow.hour, utcnow.minute, utcnow.second,tzinfo = UTC(8))
    print(UTC(8).tzname(beijing))
    print('beijing: {}'.format(beijing))

    utcTicks, uctTime = GetUtcTime()

    print(utcTicks, uctTime)
    print('year:{}, month:{}, day:{}, hour:{}, minute:{}, second:{}, weedday:{}, yearday:{}'.format(uctTime.year, uctTime.month, uctTime.day, uctTime.hour, uctTime.minute, uctTime.second, uctTime.weekday(), getYearOfDay(uctTime)))
    ts = '1569772800'
    tc = eval(ts)
    print(timestampTodatetime(tc))
    print('******************************************')
    print(time.localtime(time.time()).tm_yday)
    print(getYearOfDay(datetime.datetime.now()))

    print(operator.eq('12:00', '11:00'))
    print(operator.eq('12:00', '12:00'))
    print(operator.eq('11:00', '12:00'))