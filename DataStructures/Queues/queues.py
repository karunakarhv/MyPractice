class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop(-1)
        return None

    def sizeQueue(self):
        return len(self.items)

    def displayItems(self):
        return self.items

    def isEmpty(self):
        if self.items:
            return False
        return True

    def peek(self):
        if self.items:
            return self.items[-1]
        return None