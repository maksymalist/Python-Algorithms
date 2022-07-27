def permute(chr, arr, perm, base, iter): ## returns perm
    
    if iter == 1:
        return perm
    
    
    #n = len(arr)
    new_arr = []
    
    for i in arr:
        
        if i != chr:
            perm.append(chr+i)
        
        for j in base:
            
            if i != j and j != chr and i != chr:
                
                new_str = i+j
                new_arr.append(new_str)
            
            
    
        
        
    return permute(chr, new_arr, perm, base, iter-1)
        

def checkInclusion(s1,s2):
    
    ## get all the permutations of s1
    
    s1_arr = [char for char in s1]
    
    if len(s1_arr) == 0:
        return False
    
    if len(s1_arr) == 1:
        return s1_arr[0] in s2
    
    permutations = []

    
    for i in s1_arr:
        permutations = permutations + permute(i, s1_arr, [], s1_arr[:], len(s1))
    
    for i in permutations:
        if len(i) == len(s1_arr):
            
            if i in s2:
                print("contains")
                return True
            
    return False
    
    

if checkInclusion("ab", "bahjndn") == True:
    print("it does contain")
else:
    print("no contains")