import queue
import threading
from queue import Queue

def func1(queue):
    x = 2
    y = 5
    queue.put((x, y))

numThreads = 3
my_queue: Queue[tuple[int, int]] = Queue()
threadList = []

for i in range(numThreads):
    new_thread = threading.Thread(target=func1, args=(my_queue,))
    new_thread.start()
    threadList.append(new_thread)

for th in threadList:
    th.join()

try:
    x, y = my_queue.get(timeout=5)
    print(x, y)
except queue.Empty:
    print("No more items in queue")

try:
    x, y = my_queue.get(timeout=5)
    print(x, y)
except queue.Empty:
    print("No more items in queue")

try:
    x, y = my_queue.get(timeout=5)
    print(x, y)
except queue.Empty:
    print("No more items in queue")

try:
    x, y = my_queue.get(timeout=5)
    print(x, y)
except queue.Empty:
    print("No more items in queue")