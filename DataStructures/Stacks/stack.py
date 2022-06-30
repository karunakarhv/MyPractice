"""Stack Class
    push, pop, peek, displayItems, sizeOfStack, isEmpty
Returns:
    _type_: _description_
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def isEmpty(self):
        if self.items:
            return False
        else:
            return True

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def displayItems(self):
        return self.items

    def sizeStack(self):
        return len(self.items)

    def reverseNumber(self):
        num = list(str(self.items[0]))
        num.reverse()
        return int(''.join(num))

    def reverseString(self):
        revString = list(self.items[0])
        revString.reverse()
        return ''.join(revString)

    def paraenthsisMatching(self, expression):
        matchDic = {
            "(":")",
            "[":"]",
            "{":"}",
            ")":"(",
            "]": "[",
            "}": "{"
        }
        indCharList = list(expression)
        self.items = indCharList
        while(not self.isEmpty()):
            charPoped = self.pop()
            if matchDic[charPoped] in self.items:
                self.items.remove(matchDic[charPoped])
            else:
                return False
        return True

    def getMax(self):
        max = 0
        while(not self.isEmpty()):
            value = self.pop()
            if max < value:
                max = value
        return max