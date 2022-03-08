list1 = []
list2 = ['lte', 'sa', 'nsa']

if set(list1).issubset(list2):
    print('present')
else:
    print('not present')

value = 'lte nsa'
print(value.split(' '))