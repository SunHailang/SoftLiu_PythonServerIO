'''
    author: Sun Hai Lang
    date: 2019-09-10
'''

import requests
import ssl
import json
import urllib3
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class LeftqueryUtil(object):
    def __init__(self, requestUtil):
        self.requestUtil = requestUtil
        self.url_station = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
        self.headers = {
            'Host': 'kyfw.12306.cn',
            'If-Modified-Since': '0',
            'Pragma': 'no-cache',
            'Referer': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
    
    def station_name(self, station):
        # get station name
        print('station_name:', station)
        html_req = self.requestUtil.get(self.url_station, verify=False)
        print(html_req.status_code)
        html = html_req.text
        result = html.split('@')[1:]
        # print('station_name:', result)
        dict = {}
        for i in result:
            key = str(i.split('|')[1])
            value = str(i.split('|')[2])
            dict[key] = value
        print(dict[station])
        fo = open('station.json', 'w+')
        fo.write(json.dumps(dict))
        fo.close()
        return dict[station]
    
    def query(self, form_station, to_station, date):
        fromstation = self.station_name(form_station)
        tostation = self.station_name(to_station)
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.form_station={}&leftTicketDTO.to_station={}&purpose_code=ADULT'.format(
            date, fromstation, tostation
        )
        
        try:
            html = self.requestUtil.get(url, headers=self.headers, verify=False).json()
            result = html['data']['result']
            if result == []:
                print('Result None.')
                return ''
            else:
                print("Result Success.")
                num = 1
                for i in result:
                    info = i.split('|')
                    if info[0] != '' and info[0] != 'null':
                        print(info)
                return result
        except expression as identifier:
            return ''

if __name__ == "__main__":
    print('Strat Tickets')
    # queray = LeftqueryUtil()
    from_station = '徐州东'
    # to_station = '上海'
    # date = '2019-09-10'
    # info = queray.query(from_station, to_station, date)
    # info = queray.station_name(from_station)
    # print(info)