from heapq import heapify, heappush, heappop

# List will be used as heap
list_one = [10, 20, 30, 40]
list_two = [15, 25, 35]
list_three = [27, 29, 37, 48, 93]
list_four = [32, 33]
heap = list_one + list_two + list_three + list_four
heap.sort()

# Transform a list into heap
heapify(heap)

# Add items to heap
# heappush(heap, 10)
# heappush(heap, 30)
# heappush(heap, 20)
# heappush(heap, 400)
# heappush(heap, 5)
# heappush(heap, 6)
# heappush(heap, 7)

# Print value of the minimum element
print('Head value of heap: {}'.format(heap[0]))

# Print the elements of the heap
print('The heap elements: ')
for i in heap:
    print(i, end=' ')
print('\n')

# Pop the element
element = heappop(heap)

# Print value of the minimum element
print('Head value of heap: {}'.format(heap[0]))

# Printing the elements of heap
print('The heap elements: ')
for i in heap:
    print(i, end=' ')