def isBadVersion(v):
    if (v >= 4):
        return True
    else:
        return False

def firstBadVersion(self, n: int) -> int:
    
    low = 0
    high = 5
    mid = 0
    prev = False
    
    while low < high:
        
        mid = (high + low) // 2
        
        if isBadVersion(mid):
            prev = True
            low = mid + 1
            
        else:
            prev = False
            high = mid - 1
            