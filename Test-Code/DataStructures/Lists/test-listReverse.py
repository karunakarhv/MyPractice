list1 = ['Ing', 'Aus', 'Pty', 'Ltd']
reverseList = list1[::-1]
tempStr = ''
for idx in reverseList:
    tempStr = tempStr + idx + ' '
print(tempStr)