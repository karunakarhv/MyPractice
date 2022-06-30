data = [5,8,1,2,4,6,7]

def quick_sort(data):
    lengthData = len(data)
    if lengthData <= 1:
        return data
    else:
        pivotElement = data.pop()
        items_greater = []
        items_lower = []
        for item in data:
            if item < pivotElement:
                items_lower.append(item)
            else:
                items_greater.append(item)
    return quick_sort(items_lower) + [pivotElement] + quick_sort(items_greater)

print(quick_sort(data))