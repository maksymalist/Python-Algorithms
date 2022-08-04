
def isBadVersion(n):
    if n >= 4:
        return True
    else:
        return False

def firstBadVersion(n):
    nums = range(1, n+1)
    start = 0
    end = n+1
    
    latest = 0
    
    while end >= start:
        
        mid = (start + end) // 2
        
        if isBadVersion(mid):
            latest = mid
            end = mid - 1
            
        else:
            start = mid + 1
            
    return latest
            
[1,2,3,4,5,6,7,8,9,10,11,12]
            
            
print(firstBadVersion(12))