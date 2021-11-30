listItems = [1,1,2,-2,5,2,4,4,-1,-2,5]
listOdd = [idx for idx in listItems if idx % 2 != 0]
print(listOdd)
setOdd = set(listOdd)
print(setOdd)
mapTest = {}
for idx in setOdd:
    mapTest[idx] = listOdd.count(idx)
print(mapTest)
print(max(mapTest))

def get_middle(s):
    #your code here
    if len(s) == 1:
        return s[0]
    if len(s) % 2 == 0:
        #Even
        firstPart = s[:len(s)//2],
        secondPart = s[len(s)//2:]
        return (firstPart[0][-1] + secondPart[0])
    else:
        #Odd
        firstPart = s[:len(s)//2]
        secondPart = s[len(s)//2:]
        if len(firstPart) > len(secondPart):
            return (firstPart[0][-1])
        else:
            return (secondPart[0])