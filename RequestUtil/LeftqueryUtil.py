'''
    author: Sun Hai Lang
    date: 2019-09-10
'''

import requests
import ssl
import json, os
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
            'Cache-Control': 'no-cache',
            'Referer': 'ttps://kyfw.12306.cn/otn/leftTicket/init',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0',
            'X-Requested-With': 'XMLHttpRequest'
        }
    
    def station_name(self):
        # get station name
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
        # fo = open('station_name.json', 'w+')
        # fo.write(html)
        # fo.close()
        return dict
    
    def query(self, form_station, to_station, date):
        station_name = self.station_name()
        
        fromstation = station_name[form_station]
        print('from station name: {} -> {}'.format(form_station, fromstation))
        tostation = station_name[to_station]
        print('to station name: {} -> {}'.format(to_station, tostation))
        # https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2019-09-20&leftTicketDTO.from_station=UUH&leftTicketDTO.to_station=SHH&purpose_codes=ADULT
        url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
            date, fromstation, tostation
        )
        print('url: ', url)
        try:
            html_req = self.requestUtil.get(url, headers=self.headers, verify=False)
            print(html_req.status_code)
            print(html_req.text)
            html = json.loads(html_req.content)
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
        except:
           return 'query error.'

       

if __name__ == "__main__":
    print('Strat Tickets')
    # queray = LeftqueryUtil()
    from_station = '徐州东'
    # to_station = '上海'
    # date = '2019-09-10'
    # info = queray.query(from_station, to_station, date)
    # info = queray.station_name(from_station)
    # print(info)