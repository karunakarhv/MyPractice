def is_isogram(string):
    if string is '':
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

is_isogram("Dermatoglyphics")
