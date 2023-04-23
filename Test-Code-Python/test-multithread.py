import threading
from queue import Queue

def func1(queue):
    x = 2
    y = 5
    queue.put((x, y))

numThreads = 3
queue = Queue()
threadList = []

for th in range(numThreads):
    new_thread = threading.Thread(target=func1, args=(queue, ))
    new_thread.start()
    threadList.append(new_thread)

for th in threadList:
    th.join()

x, y = queue.get(timeout=5)
print(x, y)
x, y = queue.get(timeout=5)
print(x, y)
x, y = queue.get(timeout=5)
print(x, y)
x, y = queue.get(timeout=5)
print(x, y)