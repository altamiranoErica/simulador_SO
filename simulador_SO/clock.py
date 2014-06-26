from threading import Thread
import time

class Clock(Thread):
    
    def __init__(self, lock):
        Thread.__init__(self)
        self.observerList = {}
        self.lock = lock
        
    def addObserver(self, observer):
        self.observerList.appen(observer)
        
    def notifyObservers(self):
        for o in self.observerList:
            o.notify()
            
    def run(self):
        while 1:
            time.sleep(5)
            self.lock.acquire()
            self.notifyObservers()
            self.lock.relase()
