

import threading
import time

class MyThread(threading.Thread):

    def __init__(self, threadID, name, counter, action):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.action = action

    def run(self):
        print("srtart Thread: " + self.name)
        self.action()
        print("end Thread: " + self.name)
