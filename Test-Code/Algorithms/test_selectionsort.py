import timeit
import random

testcode = """
def selectionSort():
    listToSort = random.sample(range(10, 10000), 100000000)
    for i in range(0, len(listToSort)-2):
        pos = i
        for j in range(i+1, len(listToSort)):
            if listToSort[j] < listToSort[pos]:
                pos = j
        temp = listToSort[pos]
        listToSort[pos] = listToSort[i]
        listToSort[i] = temp
    return listToSort
"""

# print(selectionSort([5,4,3,2,1]))
print(timeit.timeit(testcode, number=10000))
