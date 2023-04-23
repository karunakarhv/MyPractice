## Convert the Grant Index List to Integer.
#
# @return SAS Grant Index List
def getSasGrantIndexListSorted():
    grantIndex = '3,5'
    # Grant Index is in String Format.
    strValue = grantIndex.split(',')
    # Removing Empty Strings from grant index list
    strValue = [idxValue for idxValue in strValue if idxValue]
    convertToIntGrantIdx = list(map(int, strValue))
    return convertToIntGrantIdx

idxList = getSasGrantIndexListSorted()
if not idxList:
    print('idxList is empty')
else:
    print(idxList)