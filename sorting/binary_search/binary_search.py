array = [1, 2, 3]
def binary_search(nums, target):
    
    low = 0
    high = len(nums) - 1
    
    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if nums[mid] < target:
            low = mid + 1

        # If x is smaller, ignore right half
        elif nums[mid] > target:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

print(binary_search(array, 2))
