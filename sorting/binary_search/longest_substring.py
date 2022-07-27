def lengthOfLongestSubstring(s):
    
    longest = 0
    
    start = 0
    end = len(s)
    
    string_arr = [char for char in s]
    
    
    while start != len(s):
        
        arr = string_arr[start:end]
        
        if len(arr) == 0:
            continue
        
        ##print(f"start:{start} end:{end} arr: {arr}")
        unique = 0
        used = []
        for i in arr:
            if i not in used:
                unique += 1
                used.append(i)
                print(f"letter: {i} used: {used} unique: {unique}")
            else:
                break
            
                
        longest = max(unique, longest)
        
        end -= 1
        
        if end == start:
            start += 1
            end = len(s)
                
            
    return longest


print(lengthOfLongestSubstring("pwwkewrtybnv"))