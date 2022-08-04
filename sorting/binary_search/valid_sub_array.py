def isValidSubsequence(array, sequence):

    if len(sequence) > len(array):
        return False

    new_arr = []

    for i in array:
        if i in sequence:
            new_arr.append(i)

    print(new_arr)
    return array == new_arr



array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(isValidSubsequence(array, sequence))