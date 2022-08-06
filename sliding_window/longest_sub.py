def longestSubstring(s):
    if len(s) <= 1:
        return len(s)
    
    longest = 0
    char_set = set()
    left = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        longest = max(longest, right - left + 1)
        
    return longest
    
print(longestSubstring("abcabcbb"))