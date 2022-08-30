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
                # For example:
                # Step 1
                # 7 is the pivot element,
                # items_lower = [5, 1, 2, 4, 6]
                # Step 2 - 6 is the pivot element
                # items_lower = [5, 1, 2, 4]
                items_lower.append(item)
            else:
                # Step 1
                # items_greater = [8]
                # Step 2
                # items_greater = []
                # Step 3
                # items_greater = [5]
                items_greater.append(item)
        print('Items Lower List - {}'.format(items_lower))
        print('Items Greater List - {}'.format(items_greater))
        print('Pivot Element - {}'.format(pivotElement))
    return quick_sort(items_lower) + [pivotElement] + quick_sort(items_greater)

print(quick_sort(data))