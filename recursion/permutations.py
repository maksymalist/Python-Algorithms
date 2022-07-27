def dfs(n, arr, perm, base, iter):
    
    if iter == 1:
        return perm
    
    new_arr = []
    
    for i in arr:
        i = str(i)
        if i != n and len(i) == len(base) - 1:
            num = [int(a) for a in str(n+i)]
            if num not in perm:
                perm.append(num) 
            perm.append(num)  
            
        for j in base:
            j = str(j)
            
            if i != j and j != n and i != n:
                new_arr.append(i+j)
    
    
    return dfs(n, new_arr, perm, base, iter-1)
    
    
    
def permute(nums):
    
    permutations = []
    
    if len(nums) == 1:
        permutations.append(nums)
        return permutations
    
    for i in nums:
        perm = dfs(str(i), nums, [], nums[:], len(nums))
        permutations = permutations + perm
        
    return permutations


perms = permute([1,2,3,4,6]) ## returns matrix of perms
print(perms)