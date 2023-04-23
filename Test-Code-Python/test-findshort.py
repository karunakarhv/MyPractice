def find_short(s):
    # your code here
    testList = s.split(' ')
    small = len(testList[0])
    for idx in range(len(testList)):
        if small > len(testList[idx]):
            small = len(testList[idx])
    return small
    #return l # l: shortest word length

print(find_short("bitcoin take over the world maybe who knows perhaps"))