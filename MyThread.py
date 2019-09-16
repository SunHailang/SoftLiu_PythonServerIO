

import threading
import time

class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def createThread(self, action, args={}):
        self.action = action
        self.args = args
        return self

    def run(self):
        self.action(self.args)
