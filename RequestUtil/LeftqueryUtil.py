'''
    author: Sun Hai Lang
    date: 2019-09-10
'''

import requests, time, datetime
import ssl

import sys, os, json
o_path = os.getcwd()
sys.path.append(o_path)

import operator

import urllib3
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from MyThread import MyThread


urllib3.disable_warnings() #不显示警告信息
ssl._create_default_https_context = ssl._create_unverified_context
req = requests.Session()

class LeftqueryUtil(object):
    def __init__(self, requestUtil):
        self.requestUtil = requestUtil
        self.url_station = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
        self.headers = {
            'Host': 'kyfw.12306.cn',
            'If-Modified-Since': '0',
            'Pragma': 'no-cache',
            'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
    
    def station_name(self, station):
        '''获取车站简拼'''
        html = requests.get(self.url_station, verify=False).text
        result = html.split('@')[1:]
        dict = {}
        for i in result:
            key = str(i.split('|')[1])
            value = str(i.split('|')[2])
            dict[key] = value
        return dict[station]

    def query(self, from_station, to_station, date):
        '''余票查询'''
        fromstation = self.station_name(from_station)
        tostation = self.station_name(to_station)
        print('from station name: {} -> {}'.format(from_station, fromstation))
        print('to station name: {} -> {}'.format(to_station, tostation))
        # https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2019-09-20&leftTicketDTO.from_station=UUH&leftTicketDTO.to_station=SHH&purpose_codes=ADULT
        url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
            date, fromstation, tostation
        )
        print('url: ', url)
        try:
            html_req = requests.get(url, headers=self.headers, verify=False)
            print(html_req.status_code)
            html = json.loads(html_req.content)
            result = html['data']['result']
            if result == []:
                print('很抱歉,没有查到符合当前条件的列车!')
                exit()
            else:
                print(date + from_station + '-' + to_station + '查询成功!')
                # 打印出所有车次信息
                num = 1  # 用于给车次编号,方便选择要购买的车次
                for i in result:
                    info = i.split('|')
                    if info[0] != '' and info[0] != 'null':
                        trainNum = info[3]
                        startTime = info[8]
                        endTime = info[9]
                        if trainNum.find("G") != -1:
                            if (startTime >= "12:00") and ((info[30] != '无' and info[30] != '') or (info[26] != '' and info[26] != '无')):
                                print(str(num) + '.' + info[3] + '车次还有余票:')
                                print('出发时间:' + startTime + ' 到达时间:' + endTime + ' 历时多久:' + info[10] + ': -> 二等座:{}, 无座:{}'.format(info[30], info[26]), end='')
                                seat = {21: '高级软卧', 23: '软卧', 26: '无座', 28: '硬卧', 29: '硬座', 30: '二等座', 31: '一等座', 32: '商务座',
                                        33: '动卧'}
                                os.system('say "your program has finish"')
                                '''
                                from_station_no = info[16]
                                to_station_no = info[17]

                                for j in seat.keys():
                                    if info[j] != '无' and info[j] != '':
                                        if info[j] == '有':
                                            print(seat[j] + ':有票 ', end='')
                                        else:
                                            print(seat[j] + ':有' + info[j] + '张票 ', end='')
                                '''
                                print('\n')
                    '''
                    elif info[1] == '预订':
                        print(str(num) + '.' + info[3] + '车次暂时没有余票')
                    elif info[1] == '列车停运':
                        print(str(num) + '.' + info[3] + '车次列车停运')
                    elif info[1] == '23:00-06:00系统维护时间':
                        print(str(num) + '.' + info[3] + '23:00-06:00系统维护时间')
                    else:
                        print(str(num) + '.' + info[3] + '车次列车运行图调整,暂停发售')
                    '''
                    num += 1
            return result
        except:
           return 'query error.'


def querayThread(args={}):
    queray = args["queray"]
    while True:
        try:
            info = queray.query(from_station, to_station, date)
            # print(info)
            print(datetime.datetime.now())
            time.sleep(5)
        except :
            pass
    os.system('say "end"')


if __name__ == "__main__":
    print('Strat Tickets')
    headers = {
            'Host': 'kyfw.12306.cn',
            'If-Modified-Since': '0',
            'Pragma': 'no-cache',
            'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
    index_url = 'https://www.12306.cn/index/'
    html_index = requests.get(index_url,headers=headers, verify=False)
    print(html_index.status_code)
    queray = LeftqueryUtil(requests)
    from_station = '宿州东'
    to_station = '上海'
    date = '2019-10-07'

    thread1 = MyThread().createThread(querayThread, args={"queray":queray})
    thread1.start()
    thread1.join()
    
    