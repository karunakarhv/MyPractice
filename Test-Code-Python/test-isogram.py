def is_isogram(string):
    if string == '':
        return True
    listItems = list(string)
    setItems = set(listItems)
    mapDict = {}
    for idx in setItems:
        mapDict[idx] = listItems.count(idx)
    for idx in mapDict:
        if mapDict[idx] > 1:
            return False
    return True

print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
