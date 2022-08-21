def threeSum(nums):
    
    def validate(arr):
        if arr[0] != arr[1] and arr[1] != arr[2] and arr[0] != arr[2]:
            if arr[0] + arr[1] + arr[2] == 0:
                return True
        return False
    
    start = 0
    out = []
    
    while start <= len(nums) - 2:
        seq = nums[start:start+3]
        
        # do shit
        if len(seq) == 3:
            if validate(seq):
                out.append(seq)
        
        start += 1
        
    return out
        
        
            
print(threeSum([-1,0,1,2,-1,-4, 5]))