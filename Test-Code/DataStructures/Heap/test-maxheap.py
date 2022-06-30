from heapq import heapify, heappush, heappop

# List will be used as heap
heap = []

# Transform a list into heap
heapify(heap)

# Add items to heap
heappush(heap, -1 * 10)
heappush(heap, -1 * 30)
heappush(heap, -1 * 20)
heappush(heap, -1 * 400)
heappush(heap, -1 * 5)
heappush(heap, -1 * 6)
heappush(heap, -1 * 7)

# Print value of the minimum element
print('Head value of heap: {}'.format(-1 * heap[0]))

# Print the elements of the heap
print('The heap elements: ')
for i in heap:
    print(-1 * i, end=' ')
print('\n')

# Pop the element
element = heappop(heap)

# Print value of the minimum element
print('Head value of heap: {}'.format(-1 * heap[0]))

# Printing the elements of heap
print('The heap elements: ')
for i in heap:
    print(-1 * i, end=' ')