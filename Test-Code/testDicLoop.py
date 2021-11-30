dictPath = {'.crt':'test.crt', '.key':'test.key', '.pem':'test.pem'}
for idx in dictPath.values():
    print(idx)

dicList = dictPath.values()
newList = []
for item in dicList:
    newList.append('/tmp/' + item)
print(newList)