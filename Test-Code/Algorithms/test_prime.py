# Algorithm to find the prime numbers
# Given the number N, print whether the number is prime number or not.
from math import sqrt

def isPrimeNum(num):
    primeFlag = True
    if num == 1 or num == 0 or num == 2:
        return True
    for i in range(2, int(sqrt(num))+1):
        print(num, i)
        if num % i == 0:
            primeFlag = False
            break
        primeFlag = True
    return primeFlag

def generateListOfPrimeNum(length):
    primeList = []
    # Generate List of Prime Number
    for i in range(0, length):
        if isPrimeNum(i):
            primeList.append(i)
    return primeList

# for i in range(0, 20):
#     print('{} is prime {}'.format(i, isPrimeNum(i)))

print(generateListOfPrimeNum(20))