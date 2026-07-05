
from threading import Thread,Semaphore

import time

sem = Semaphore(2)

def worker(name):
    print(name," is waiting")

    sem.acquire()

    print(name," entered ")

    time.sleep(3)

    print(name, " Leaving")

    sem.release()

for i in range(5):
    t = Thread(target=worker,args=(f"Thread - {i+1}",))
    t.start()
    
t.join()



