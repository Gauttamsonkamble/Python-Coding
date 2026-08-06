
from multiprocessing import Process,Queue

def sender(q):
    q.put("Hello from process 1")

def reciever(q):
    print(q.get())

if __name__=="__main__":
    q = Queue()

    p1 = Process(target=sender,args=(q,))
    p2 = Process(target=reciever,args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

