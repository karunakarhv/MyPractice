dictItems = {'a': 1, 'b': 2}

val = 3

if val in dictItems.values():
    print(True)
else:
    print(False)
    
days = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

for day, value in days.items():
    print(day, value)