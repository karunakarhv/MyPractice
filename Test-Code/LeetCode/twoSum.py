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

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rList = []
        totalSum = 0
        for index in range(len(nums)):
            j = index + 1
            while(j <= (len(nums) - 1)):
                totalSum = nums [index] + nums[j]
                if totalSum == target:
                    rList.append(index)
                    rList.append(j)
                    return rList
                j = j + 1
        return rList

    def returnValue(l1):
        strValue = ''
        while(l1.next != None):
            strValue = strValue + str(l1.value)
        return strValue

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstValue = ''
        secondValue = ''
        firstValue = self.returnValue(l1)
        secondValue = self.returnValue(l2)
        firstList = [int(x) for x in str(firstValue)]
        secondList = [int(x) for x in str(firstValue)]
        reverseFirstList = firstList[::-1]
        reverseSecondList = secondList[::-1]
        for idx in range(len(reverseFirstList)):
             firstValue = firstValue + (str(reverseFirstList[idx]))
        for idx in range(len(reverseSecondList)):
            secondValue = secondValue + (str(reverseSecondList[idx]))
        resultList = [int(x) for x in str(int(firstValue) + int(secondValue))]
        objectList = List()
        for val in resultList:
            objectList.insert(val)
        return objectList



if __name__ == "__main__":
    l1 = [3,2,4]
    l2 = [5, 6, 7]
    obj = Solution()
    print(obj.addTwoNumbers(l1, l2))
