from operator import truediv


def bubble_sort(arr):
    
    n = len(arr) -1
    swapped = False
    
    while not swapped:
        swapped = True
        
        for i in range(n):
            if arr[i] > arr[i+1]:
                swapped = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
                
arr = [7,2,8,9,-1,7,0,10,45,3,2]  
print(arr)        
bubble_sort(arr)
print(arr)