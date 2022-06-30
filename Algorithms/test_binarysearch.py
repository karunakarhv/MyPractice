# Already sorted sequence
mylist = [1,2,3,4,5,6,7]

def binary_search(mylist, item):
    begin_idx = 0
    end_idx = len(mylist) - 1
    while begin_idx <= end_idx:
        midPoint = begin_idx + (end_idx - begin_idx) // 2
        midPointValue = mylist[midPoint]
        if midPointValue == item:
            return midPoint
        elif item < midPointValue:
            end_idx = midPoint - 1
        else:
            begin_idx = midPoint + 1
    return None

print(binary_search(mylist, 5))