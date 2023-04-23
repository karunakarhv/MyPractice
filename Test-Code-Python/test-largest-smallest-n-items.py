# Find the Largest or Smallest of N items
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name':'APPLE', 'shares':100, 'price': 91.1},
    {'name':'IBM', 'shares':20, 'price': 10.1},
    {'name':'Tesla', 'shares':120, 'price': 200.01},
    {'name':'Gold', 'shares':200, 'price': 250.02},
    {'name':'Samsung', 'shares':300, 'price': 21.1},
]

print('Smallest ',heapq.nsmallest(3, portfolio, key=lambda s:s['price']))
print('Largest ', heapq.nlargest(3, portfolio, key=lambda s:s['price']))