def merge_sort(nums):
    
    if len(nums) > 1:
        
        mid = len(nums) // 2
        left = nums[0:mid]
        right = nums[mid:len(nums)]
        
        # recursion
        merge_sort(left)
        merge_sort(right)
        
        # merge
        i = 0 # left numsay index
        j = 0 # right numsay index
        k = 0 # merged numsay index
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j+=1

            k+=1
            
            
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
    
    
    
    
    
    
    
nums = [2,4,7,9,5,3]
merge_sort(nums)
print(nums)