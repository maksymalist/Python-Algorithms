def searchMatrix(matrix, target):
    
    start = 0
    end = len(matrix) -1
    
    def binary_search(arr, target):
        
        low = 0
        high = len(arr) -1
        
        while high >= low:
            
            mid = (low+high)//2
            if arr[mid] == target:
                return True
            
            if arr[mid] > target:
                high = mid - 1
            
            if arr[mid] < target:
                low = mid + 1
            
        return False
    
    while end >= start:
        
        mid = (start + end) // 2
        l, r = matrix[mid][0], matrix[mid][-1]
        
        if target >= l and target <= r:
            arr = matrix[mid]
            return binary_search(arr, target)
                
        
        if target > r:
            start = mid + 1
            
        if target < l:
            end = mid - 1
            
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(matrix, 11))