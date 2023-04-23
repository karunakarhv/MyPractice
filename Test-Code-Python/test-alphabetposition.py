import string
def alphabet_position(text):
    text = text.lower()
    print(text)
    listItems = list(text)
    print(listItems)
    value = ''
    if len(listItems) == 1:
        if listItems[0].isspace():
            value = ''
        if listItems[0].isdigit():
            value = ''
        if not listItems[0].isalpha():
            value = ''
        else:
            value = string.ascii_lowercase.index(listItems[0])
            value = value + 1
        return (value)
    else:
        for idx in listItems[:-1]:
            if idx.isspace():
                print('Space')
                continue
            if idx.isdigit():
                value = ''
                print('Digit')
                continue
            if not idx.isalpha():
                listItems.remove(idx)
                print('Not alpha')
                continue
            print(value)
            print(string.ascii_lowercase.index(idx))
            value = value + str(string.ascii_lowercase.index(idx)+1) + ' '
    print(repr(value.rstrip()))
    return value.rstrip()

# def alphabet_position(text):
def alphabet_position(text):
    value = ''
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    listItems = list(text)
    if len(listItems) == 1:
        if listItems[0].isspace():
             value = ''
        if listItems[0].isdigit():
             value = ''
        if not listItems[0].isalpha():
             value = ''
        else:
            value = string.ascii_lowercase.index(listItems[0])
            value = value + 1
        return (value)
    for i in text:
        # Performing AND operation
        # with number 31
        andOperationValue = str((ord(i) & 31))
#        print(andOperationValue)
        if andOperationValue == '0':
            continue
        value = value + andOperationValue  + ' '
    print(repr(value.rstrip()))
    return value

#alphabet_position("The sunset sets at twelve o' clock.")
alphabet_position("The narwhal bacons at midnight.")
# alphabet_position("123")
#alphabet_position("A")
#alphabet_position("B")
#alphabet_position("pXwCnqPVgNShWkkgNKsYAyzQaXBjETJtAWyvYjcqyKimSFDaGEwBiJpTpKIFWVKFtPruNXMvChCbvVOLNqkJTAKKIGLkgFFUtvLg")