def permute(arr):
    result = []
    if len(arr) == 1:
        return [arr[:]]
    
    
    for i in arr:
        n = arr.pop(0)
        perms = permute(arr)
        
        
        for perm in perms:
            perm.append(n)
        result = result + perms
        arr.append(n)
        
    return result
        
        
print(permute(["a", "b", "c", "d", "e", "f"]))
    