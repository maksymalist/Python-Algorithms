nums =  [3,4,5,1,2]
nums = [5,1,2,3,4]
def solution(nums):
    low = 0
    high = len(nums) - 1

    while high >= low:
        
        mid = (high+low)//2
        print(nums[low], nums[mid], nums[high])
        
        if high == low:
            return nums[mid]
        
        if nums[mid] <= nums[high] and nums[mid] <= nums[low]:
            return nums[mid]
        
        if nums[high] < nums[low]:
            low = mid + 1
            continue
            
        if nums[high] > nums[low]:
            high = mid - 1
            
        
        
    


print(solution(nums))


# nums = [3,4,5,6,7,8,0,1,2]


# def solution(nums):
#     mn = nums[0]
#     low = 0
#     high = len(nums) - 1

#     while high > low:
#         print(low, " -> ", high)
#         mid = (high+low) // 2
#         right = mid + 1
#         left = mid - 1
        
#         mn = min(left, right, mid)
        
        
#         if mid < left and mid < right:
#             mn = nums[mid]
#             break
        
        
#         elif mid > left and mid > right:   
            
#             smallest = min(left, right)
            
#             if smallest == left:
#                 high = left
#             if smallest == right:
#                 low = right
                
        
#         elif left < right:
#             high = left
            
#         elif right < left:
#             low = right
            
        
        
            
#     return mn
    


# print(solution(nums))