def three_sum(nums):
    res = []
    nums.sort()
    
    # sort trough each num in arr
    for i, a in enumerate(nums):
        
        # remove duplicates
        if i > 0 and a == nums[i-1]:
            continue
        
        # binary search with 2 pointers
        
        start, end, = i+1, len(nums) -1
        
        while end > start:
            t_sum = nums[start] + a + nums[end]
            if t_sum == 0:
                res.append([nums[start], a, nums[end]])
                end-=1
                while nums[end] == nums[end-1]:
                    end -= 1
                
            if t_sum < 0:
                start +=1
                
            if t_sum > 0:
                end -= 1
                
    return res
            
            
        
        


arr = [-1,0,1,2,-1,-4, 4, 9, 3, 6, 3,3,3,3,3,3,3,3,3]
print(three_sum(arr))