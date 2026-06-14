
import threading 
import time

class MyThread ( threading.Thread):
    def run(self):
        print("Thread Running ")
        time.sleep(3)
        print(" Thread 1 Finished")


class MyThread2 ( threading.Thread):
    def run(self):
        print("Thread 2 Running ")
        time.sleep(3)
        print("Thread 2 Finished")

class MyThread3 ( threading.Thread):
    def run(self):
        print("Thread 3 Running ")
        time.sleep(3)
        print("Thread 3 finished")


t = MyThread()
t2 = MyThread2()
t3 = MyThread3()

t.start()
t2.start()
t3.start()

t.join()
t2.join()
t3.join()


