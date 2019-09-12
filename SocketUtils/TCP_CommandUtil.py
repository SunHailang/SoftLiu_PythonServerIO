'''
    author: Sun Hai Lang
    date: 2019-09-10
'''

import sys, os, json
o_path = os.getcwd()
sys.path.append(o_path)

from RequestUtil.LeftqueryUtil import LeftqueryUtil
from RequestUtil.LoginUtil import LoginUtil

from RequestUtil import RequestIO

class TCP_CommandUtil(object):

    def __init__(self, command):
        self.command = command
        self.requestUtil = RequestIO.req
        print(self.command)
        self.code = self.command['code']
        self.actionRun = self.createRun()
        

    def createRun(self):
        run = {
            'TrainLogin': self.runTrainLogin,
            'TrainQuery': self.runTrainQuery
        }
        if (self.code in run.keys()):
            return run[self.code]          
        else:
            return None
        

    def runTrainLogin(self):
        user_name = self.command['user_name']
        user_password = self.command['user_password']

        login = LoginUtil(self.requestUtil, user_name, user_password)
        login.showimg()
        print('  =============================================================== ')
        print('   根据打开的图片识别验证码后手动输入，输入正确验证码对应的位置 ')
        print('     --------------------------------------')
        print('            1  |  2  |  3  |  4 ')
        print('     --------------------------------------')
        print('            5  |  6  |  7  |  8 ')
        print('     --------------------------------------- ')
        print(' =============================================================== ')
        answer_num = input('Please input check code: ')
        login.captcha(answer_num)

        result = {
            'status': 0,
            'user_name': user_name,
            'user_password': user_password
        }
        return result

    def runTrainQuery(self):

        from_station = self.command['from_station']
        to_station = self.command['to_station']
        date = self.command['date']

        queray = LeftqueryUtil(self.requestUtil)
        info = queray.query(from_station, to_station, date)

        result = {
            'status': 0,
            'result': info
        }
        return result

    def getResult(self):

        if self.actionRun == None:
            params = {
                'status': -1
            }
            result = json.dumps(params)
        else:
            result = self.actionRun()
        return result

if __name__ == "__main__":
    pram = {
        'code': 'TrainLogin',
        'user_name': 'user_name',
        'user_password': 'user_password'
    }
    js = json.dumps(pram)
    com = TCP_CommandUtil(json.loads(js))
    result = com.getResult()
    print(result)