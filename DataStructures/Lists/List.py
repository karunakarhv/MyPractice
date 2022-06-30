
class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class List(object):
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = ListNode(val, next=None)
        else:
            node = self.head
            while(node.next != None):
                node = node.next
            tempNode = ListNode(val, None)
            node.next = tempNode

    def displayList(self):
        node = self.head
        while(node.next != None):
            node = node.next

if __name__ == "__main__":
    objectList = List()
    objectList.insert(1)
    objectList.insert(2)
    objectList.insert(3)
    objectList.displayList()