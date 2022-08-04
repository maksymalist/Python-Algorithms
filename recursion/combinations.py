def dfs(n, arr, perm, base, iter, k):
    
    if iter == 1:
        return perm
    
    new_arr = []
    
    for i in arr:
        i = str(i)
        if i != n and len(i) == k -1:
            num = [int(a) for a in str(n+i)]
            if num not in perm:
                perm.append(num) 
            
        for j in base:
            j = str(j)
            
            if i != j and j != n and i != n:
                new_arr.append(i+j)
    
    
    return dfs(n, new_arr, perm, base, iter-1, k)
    
    
    
def permute(n, k):
    
    nums = list(range(1,n+1))
    permutations = []
    
    if len(nums) == 1:
        permutations.append(nums)
        return permutations
    
    for i in nums:
        perm = dfs(str(i), nums, [], nums[:], len(nums), k)
        permutations = permutations + perm
        
    return permutations


perms = permute(5, 5) ## returns matrix of perms
print(perms)