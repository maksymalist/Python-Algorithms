def checkInclusion(s1, s2):
    
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
    
    perms = permute([char for char in s1])
    
    for perm in perms:
        p = "".join(perm)
        if p in s2:
            return True
        
    return False


print(checkInclusion("hadb","abdahbdhdd"))