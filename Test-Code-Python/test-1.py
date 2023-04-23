# string = "wss://192.168.11.1:35560/notification"
# newstring = string.replace('wss://', '')
# newstring = newstring.replace('/notification', '')
# print(newstring)

# myDict = {'a':1, 'b':2}
# for key, value in myDict.items():
#     print(key, value)

testList = [{'tcName': 'WINNF.FT.C.REG.1', 'isMultiStep': True},
                {'tcName': 'WINNF.FT.C.REG.5', 'isMultiStep': False},
                {'tcName': 'WINNF.FT.C.REG.8', 'isMultiStep': True},
                {'tcName': 'WINNF.FT.C.REG.10', 'isMultiStep': False},
                {'tcName': 'WINNF.FT.C.REG.12','isMultiStep': False},
                {'tcName': 'WINNF.FT.C.REG.14', 'isMultiStep': False},
                {'tcName': 'WINNF.FT.C.REG.16', 'isMultiStep': False},
                {'tcName': 'WINNF.FT.C.REG.18', 'isMultiStep': True},
]

for test in testList:
    print(test['tcName'])

mylist = ["A","B","C","D","E"]

for idx, element in enumerate(testList):
    prevElement = testList[idx-1] if idx > 0 else None
    curElement = element
    nextElement = testList[idx+1] if idx < len(testList)-1 else None
    if prevElement is None or nextElement is None:
        continue
    if prevElement['isMultiStep'] != curElement['isMultiStep']:
        print(prevElement, curElement)