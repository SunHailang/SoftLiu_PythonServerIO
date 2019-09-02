

import threading
import time

class MyThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def createThread(self, action, args={}):
        self.action = action
        self.args = args
        return self

    def run(self):
        print("srtart Thread: " + self.name)
        self.action(self.args)
        print("end Thread: " + self.name)
