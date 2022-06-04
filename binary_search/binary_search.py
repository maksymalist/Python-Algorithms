array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low < high:
        mid = (low + high) // 2
        if array[mid] == target:
            print("Found target")
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print("Target not found")
    return -1


binary_search(array, 5)