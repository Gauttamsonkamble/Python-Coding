
import threading

import time

lock = threading.Lock()

def speak(name):
    lock.acquire()
    for i in range(3):
        print(name, " is Speaking")
        
    lock.release()

t1 = threading.Thread(target=speak,args=("Student 1",))

t2 = threading.Thread(target=speak,args=("Student 2",))

t1.start()
t2.start()

t1.join()
t2.join()

