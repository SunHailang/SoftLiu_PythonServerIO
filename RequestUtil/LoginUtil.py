'''
    author: Sun Hai Lang
    date: 2019-09-09
'''

import requests
import ssl
import json
import urllib3
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import RequestIO

class Login(object):

    def __init__(self, reqestUtil, username, password):
        self.reqestUtil = reqestUtil
        self.username = username
        self.password = password
        self.url_pic = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_sit=E&module=login%rand=sjrand&0.15905700266966694'
        self.url_check = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
        self.url_login = 'https://kyfw.12306.cn/passport/web/login'
        self.headers = {
                'Host':'kyfw.12306.cn',
                'Referer':'https://kyfw.12306.cn/otn/login/init',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
                }

    def showimg(self):
        # show image
        html_pic = self.reqestUtil.get(self.url_pic, headers=self.headers).content
        open('pic.jpg', 'wb').write(html_pic)

        img = mpimg.imread('pic.jpg')
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    
    def captcha(self, answer_num):
        # check code
        answer_sp = answer_num.split(',')
        answer_list = []
        an = {
            '1': (31, 35),
            '2': (116, 46),
            '3': (191, 24),
            '4': (243, 50),
            '5': (22, 114),
            '6': (117, 94),
            '7': (167, 120),
            '8': (251, 105)
        }
        for i in answer_sp:
            for j in an.keys():
                if i == j:
                    answer_list.append(an[j][0])
                    answer_list.append(',')
                    answer_list.append(an[j][1])
                    answer_list.append(',')
        s = ''
        for i in answer_list:
            s += str(i)
        answer = s[:-1]
        form_check = {
            'answer': answer,
            'login_site': 'E',
            'rand': 'sjrand'
        }
        result = -1
        try:
            loginpost = self.reqestUtil.post(self.url_login, data=form_check, headers=self.headers)
            print(loginpost.text)
            html_login = json.loads(loginpost.text)
            print(html_login)
            if html_login['result_code'] == 0:
                print('login success.')
                result = 0
            else:
                print('login failed.')
        finally:
            return result
        


