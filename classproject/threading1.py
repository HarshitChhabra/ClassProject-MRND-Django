import sys,time,threading


counter = 0
def activity(tag):
    global counter
    thread_id = threading.current_thread().ident
    for i in range(5):
        time.sleep(0.1)
        counter+=1
        #time.sleep(0.1)
        print('Hello from',tag,"i = ",i,"thread_id = ",thread_id,'counter = ',counter)
        #time.sleep(2)

def incCount():
    global counter
    for i in range(10):
        counter+=1
        time.sleep(1)

def watcher():
    global counter
    while True:
        print('Count is ',counter)
        time.sleep(1)

def worker1():
    print('worker 1 thread id is ', threading.current_thread().ident)
    #activity('worker1')
    incCount()

def worker2():
    print('worker 2 thread id is ',threading.current_thread().ident)
    #activity('worker2')
    incCount()

def main():
    print('Main thread is ',threading.current_thread().ident)
    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)
    thread3 = threading.Thread(target=watcher)
    thread1.start()
    thread2.start()
    thread3.start()

if __name__ == '__main__':
    main()