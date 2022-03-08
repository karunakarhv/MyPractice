list1 = [[1,2,3], [4,5,6], [7,8,9]]

for item in list1:
    print(item[0], item[1], item[2])
anotherList = [10,11,12]
list1.insert(1, anotherList)

print(list1)