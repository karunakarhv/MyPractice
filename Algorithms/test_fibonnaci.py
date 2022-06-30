import datetime
# Algorithm to calculate fibonacci
# 0, 1, 1, 2, 3, 5

def recursiveFibonacci(num):
    # Base Condition
    if num == 0:
        return 0
    if num == 1:
        return 1
    # General Condition
    return recursiveFibonacci(num - 1) + recursiveFibonacci(num - 2)

def calculateSum(mylist):
    totalSum = 0
    for i in mylist:
        totalSum = totalSum + mylist[i]
    return totalSum

def fibonnaci(length_of_series):
    myList = []
    sum = 1
    if length_of_series == 3:
        return [0, 1, 1]
    elif length_of_series == 1:
        return [0]
    elif length_of_series == 2:
        return [0, 1]
    myList = [0, 1, 1]
    for i in range(3, length_of_series):
        sum = myList[-1] + myList[-2]
        myList.insert(i, sum)
    return calculateSum(myList)

print(fibonnaci(1))
print(fibonnaci(2))
print(fibonnaci(3))
startTime = datetime.datetime.now()
print(fibonnaci(4))
endTime = datetime.datetime.now()
print(f'Total Time = {endTime - startTime}')

print(recursiveFibonacci(3))
