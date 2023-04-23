import copy

# = assignment operator
def equalTo():
    list1 = [1,2,3,4,5]
    list2 = list1
    print('Address - list1', id(list1))
    print('Address - list2', id(list2))
    list2[0] = 1000
    print(list1)
    print(list2)
    print('Address - list1', id(list1))
    print('Address - list2', id(list2))

# shallow copy assignment operator
def shallowCopy():
    list1 = [[1,2,3,4,5],[1,2,3,4,5]]
    list2 = copy.copy(list1)
    print('Address - list1', id(list1))
    print('Address - list2', id(list2))
    list1[0][1] = 100
    list2[0][1] = 1000
    list1.append([4,5,6,7])
    print(list1)
    print(list2)
    print('Address - list1', id(list1))
    print('Address - list2', id(list2))

# Deep copy assignment operator
def deepCopy():
    list1 = [[1,2,3,4,5],[1,2,3,4,5]]
    list2 = copy.deepcopy(list1)
    print('Address - list1', id(list1))
    print('Address - list2', id(list2))
    list1[0][1] = 100
    list2[0][1] = 1000
    list1.append([4,5,6,7])
    print(list1)
    print(list2)
    print('Address - list1', id(list1))
    print('Address - list2', id(list2))

shallowCopy()
deepCopy()