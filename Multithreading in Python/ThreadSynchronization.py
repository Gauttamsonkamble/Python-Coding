
import threading

import time

counter = 0

lock = threading.Lock()



def increase():
    global counter

    for i in range(5):
        lock.acquire()
        counter += 1

        print(counter)
        lock.release()



t1 = threading.Thread(target=increase)

t2 = threading.Thread(target=increase)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Value",counter)