'''
    author: Sun Hai Lang
    date: 2019-09-10
'''

from RequestUtil.LeftqueryUtil import LeftqueryUtil

class TCP_CommandUtil(object):

    def __init__(self, command):
        self.command = command
        print(self.command)
        self.code = self.command['code']
        
        self.actionRun = self.createRun()

    def createRun(self):
        run = {
            'Tickets': self.runTickets()
        }
        return run[self.code]

    def runTickets(self):

        from_station = self.command['from_station']
        to_station = self.command['to_station']
        date = self.command['date']

        queray = LeftqueryUtil()
        info = queray.query(from_station, to_station, date)

        result = {
            'status': 0,
            'result': info
        }

        return result

    def getResult(self):

        result = self.actionRun()

        return result