def move_zeros(array):
    zeroList = [0] * array.count(0)
    array = [i for i in array if i != 0]
    print(array)
    array = array + zeroList
    return array

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))