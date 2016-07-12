#!/Python27/python

import Queue
import threading
from threading import Thread
import time
import ctypes


exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
    
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def MBox(title, text, style):
    MBox = ctypes.windll.user32.MessageBoxA(0, text, title, style)
    

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)

            for i in range(0,5):
                MBox('Virus Detected!', 'Restart your computer now.', 0)
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Virus-1", "Virus-2", "Virus-3", "Virus-4", "Virus-5"]
nameList = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in range(0,1000):
    thread = myThread(threadID, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"