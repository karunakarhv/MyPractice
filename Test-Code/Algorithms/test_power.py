import datetime
# Algorithm to compute base power of n

def power(base, num):
    # 2^3 = 2 * 2^2 = 2 * 2 * 2^1 = 2 * 2 * 2 * 2^0
    product = 1
    for i in range(0, num):
        product = product * base
    return product

def recursivePower(base, num):
    # Base Condition
    if num == 0:
        return 1
    # General Condition
    return base * recursivePower(base, num - 1)

startTime = datetime.datetime.now()
print(power(2, 1000))
endTime = datetime.datetime.now()
print(f'Total Time = {endTime - startTime}')
startTime = datetime.datetime.now()
print(recursivePower(2, 500))
endTime = datetime.datetime.now()
print(f'Total Time Recursive = {endTime - startTime}')