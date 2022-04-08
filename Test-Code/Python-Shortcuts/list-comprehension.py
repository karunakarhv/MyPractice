l1 = [1, 2, 3, 4, 5, 6]
l1[:] = [ 1 if (x%2 == 0) else 0 for x in l1]
print(l1)