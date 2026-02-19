# Practice Threading and Multiprocessing
import os
import threading
import time
import psutil
# Define a custom thread class that inherits from threading.Thread
# This class will override the run() method to define the thread's behavior
class MyThreadClass(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name

    def run(self):
        print(f"Starting thread: {self.name}")
        # Simulate some work
        time.sleep(2)
        print(f"Exiting thread: {self.name}")
    
# Create and start threads
for threadId in range(3):
    thread1 = MyThreadClass(1, "Thread-1")
    thread2 = MyThreadClass(2, "Thread-2")
    thread1.start()
    thread2.start()
# Wait for threads to complete
thread1.join()
thread2.join()
print("All threads completed.")

for t in range(3):
    p = psutil.Process(os.getpid())
    mem_info = p.memory_info()
    print(f"Memory usage after thread {t+1}: RSS={mem_info.rss}, VMS={mem_info.vms}")

