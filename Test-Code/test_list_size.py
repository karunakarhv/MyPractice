import sys

l1 = [10,20,30,40,50,60,70,80,90,100]
l2 = [10,20,30,40,50,60,70,80,90,100]
t1 = (10,20,30,40,50,60,70,80,90,100)
t2 = (10,20,30,40,50,60,70,80,90,100)

print('List Size', sys.getsizeof(l1))
print('Tuple Size', sys.getsizeof(t1))
print('List - Address', id(l1))
print('List - Address', id(l2))
print('Tuple - Address', id(t1))
print('Tuple - Address', id(t2))