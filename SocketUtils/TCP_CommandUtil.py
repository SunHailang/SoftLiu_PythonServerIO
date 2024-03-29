'''
    author: Sun Hai Lang
    date: 2019-09-10
'''

import base64

import sys, os, json
# o_path = os.getcwd()
# sys.path.append(o_path)

from RequestUtil.LeftqueryUtil import LeftqueryUtil
from RequestUtil.LoginUtil import LoginUtil
from RequestUtil.LoginUtil import LoginCheckCode

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
            'TrainCheckCodeType': self.runTrainCheckCode,
            'TrainLoginType': self.runTrainLogin,
            'TrainQueryType': self.runTrainQuery
        }
        if (self.code in run.keys()):
            return run[self.code]          
        else:
            return None
        
    def runTrainCheckCode(self):
        # checkCode = LoginCheckCode(self.requestUtil)
        # img = checkCode.showimg()
        with open('Resources/pic.jpg', 'rb') as fo:
            img = fo.read()
        
        base64_img = base64.b64encode(img)
        base64_string = base64_img.decode('utf-8')

        info = {
            'code': self.code,
            'status': 0,
            'result': base64_string
        }
        result_info = json.dumps(info).encode('utf-8')
        result = {            
            'result': result_info,
            'size': len(result_info)
        }
        print(len(img))
        return result

    def runTrainLogin(self):
        user_name = self.command['user_name']
        user_password = self.command['user_password']

        info = {
            'code': self.code,
            'status': 0,
            'user_name': user_name,
            'user_password': user_password
        }
        result_info = json.dumps(info).encode('utf-8')
        result = {            
            'result': result_info,
            'size': len(result_info)
        }
        return result

    def runTrainQuery(self):

        from_station = self.command['from_station']
        to_station = self.command['to_station']
        date = self.command['date']

        queray = LeftqueryUtil(self.requestUtil)
        info = queray.query(from_station, to_station, date)

        info = {
            'code': self.code,
            'status': 0
        }
        result_info = json.dumps(info).encode('utf-8')

        result = {
            'result': result_info,
            'size': len(result_info)
        }
        return result

    def getResult(self):

        if self.actionRun == None:
            params = {
                'code': self.code,
                'status': -1
            }
            result_info = json.dumps(params).encode('utf-8')
            result = {
                'result': result_info,
                'size': len(result_info)
            }
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