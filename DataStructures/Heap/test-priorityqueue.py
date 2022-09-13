import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # Value Index is given if the 2 items inserted has the same priority
        # Priority is negated because heapq is implemented in
        # such a manner that when it pops it returns the smallest element.
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.push(Item('fooTest'), 2)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())