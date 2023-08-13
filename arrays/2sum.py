nums = [2,3,5,6,19,4]
sm = 25



def solution(nums, s):

    hm = {}
    
    for n in nums:
        if n in hm:
            return [hm[n], n]
        else:
            hm[s-n] = n
            
    return -1



print(solution(nums, sm))


// 




