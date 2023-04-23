employeeCode = ['1225875', '1225875', '1225876', '1225876', '1225877']

def has_duplicates(lst):
    return len(lst) == len(set(lst))

print(has_duplicates(employeeCode))
