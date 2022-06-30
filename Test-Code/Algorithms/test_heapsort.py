# Heap Implementation

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # Largest so far is compared with left child
    if left < n and arr[largest] < arr[left]:
        largest = left

    # Largest so far is compared with right child
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change parent
    if largest != i:
        # SWAP
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursive call
        max_heapify(arr, n, largest)



# Driver Code
arr = [2, 15, 4, 30, 18, 6, 25]
n = len(arr)

# Build a max heap
for i in range(n//2-1, -1, -1):
    max_heapify(arr, n, i)

def heap_sort(arr, n):
    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

# heap sort
heap_sort(arr, n)

# Display
print("Sorted Array is")
for i in range(n):
    print(arr[i])