arr = [21, 4, 1, 3, 9, 8, 25, 0, 6, 2]


def bubble_sort(arr):
    
    n = len(arr) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0, n):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]


print(arr)
bubble_sort(arr)
print(arr)