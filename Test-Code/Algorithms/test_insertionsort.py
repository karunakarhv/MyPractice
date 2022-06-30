def insertion_sort(listToSort):
    length = range(1, len(listToSort))
    for i in length:
        value_to_sort = listToSort[i]
        while listToSort[i-1] > value_to_sort and i > 0:
            listToSort[i], listToSort[i-1] = listToSort[i-1], listToSort[i]
            i = i - 1

    return listToSort

print(insertion_sort([9,8,7,6,5,4,3,2,1]))