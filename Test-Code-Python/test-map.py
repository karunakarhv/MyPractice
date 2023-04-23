import re
# Map(function, iterables)
list1 = [1, 2, 3, 4]
list2 = ['test?!', 'test!!!!...', 'how are you?']

def removePunctuation(word):
    return re.sub(r'[?!.;"()-]', "", word)

print(list(map(lambda x: x * x, list1)))
print(list(map(removePunctuation, list2)))