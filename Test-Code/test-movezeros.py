def move_zeros(array):
    zeroList = [0] * array.count(0)
    array = [i for i in array if i != 0]
    array = array + zeroList
    return array

move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])