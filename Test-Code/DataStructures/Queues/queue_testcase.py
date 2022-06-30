import unittest
from queues import Queue
import datetime

class QeueueTestCase(unittest.TestCase):

    def setUp(self):
        self.myQueue = Queue()

    def test_peek(self):

        self.myQueue.enqueue(1)
        self.myQueue.enqueue(2)
        self.myQueue.enqueue(3)
        self.assertEqual(self.myQueue.peek(), 1)

    def test_sizeOfStack(self):

        self.myQueue.enqueue(1)
        self.myQueue.enqueue(2)
        self.myQueue.enqueue(3)
        self.assertEqual(self.myQueue.sizeQueue(), 3)

    def test_push(self):

        self.myQueue.enqueue(1)
        self.myQueue.enqueue(2)
        self.myQueue.enqueue(3)
        self.assertEqual(self.myQueue.displayItems(), [3, 2, 1])

    def test_pop(self):

        self.myQueue.enqueue(1)
        self.myQueue.enqueue(2)
        self.myQueue.enqueue(3)
        self.myQueue.dequeue()
        self.assertEqual(self.myQueue.displayItems(), [3, 2])

    def test_isEmpty(self):

        self.myQueue.enqueue(1)
        self.myQueue.enqueue(2)
        self.myQueue.enqueue(3)
        self.myQueue.dequeue()
        self.myQueue.dequeue()
        self.myQueue.dequeue()
        self.assertTrue(self.myQueue.isEmpty())

    def test_time_to_insert(self):
        timeNow = datetime.datetime.now()
        for i in range(0, 1000000):
            self.myQueue.enqueue(i)
        timeAfter = datetime.datetime.now()
        print(f'Time Taken to insert {timeAfter-timeNow}')

if __name__ == "__main__":
    unittest.main()