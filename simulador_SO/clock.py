from threading import Thread
import time

class Clock(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.observerList = {}
        
    def addObserver(self, observer):
        self.observerList.appen(observer)
        
    def notifyObservers(self):
        for o in self.observerList:
            o.notify()
            
    def run(self):
        time.sleep(5)
        self.notifyObservers()
        
            
    
    
