from threading import Thread
from datetime import datetime
import time
import threading

def one(index):
    print('Enter Input for thread {}'.format(index))
    testCaseName =  "WINNF.FT.C.REG.10"
    currentTime = datetime.utcnow().replace(microsecond=0).isoformat()
    print(testCaseName+'_'+currentTime+'.'+'log')
    time.sleep(2)

def two():
    while True:
        print('Enter Input for thread 2')
        ans = input()
        print(ans)
        time.sleep(2)

for i in range(0, 2):
    t = Thread(target=one, args=(i,))
    t.start()
    t.join()
    print(threading.active_count())
    print('helo')
    time.sleep(10)