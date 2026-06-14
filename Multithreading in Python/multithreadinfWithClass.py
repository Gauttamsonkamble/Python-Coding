
import threading

import time

class MyThread (threading.Thread):
    def run(self):
        print("Thread is Running ")
        time.sleep(2)

t = MyThread()

t.start()

t.join()