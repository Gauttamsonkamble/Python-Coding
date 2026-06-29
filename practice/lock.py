
import threading

counter = 0

lock = threading.Lock()

def increament():
    global counter
    print("Thread 1")

    for _ in range(100000):
        with lock:
            counter += 1

def increament2():
    global counter
    print("Thread 2")

    for _ in range(100000):
        with lock:
            counter += 2


t1 = threading.Thread(target=increament)
t2 = threading.Thread(target=increament2)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)