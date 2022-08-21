def isValid(s):

    stack = []
    pairs = { ")": "(", "}": "{", "]": "[" }
    
    for i in s:
        if i in ["(","{","["]:
            stack.append(i)
            
        else:
            check = pairs[i]
            
            if len(stack) > 0 and check == stack[len(stack)-1]:
                stack.pop()
                
            else:
                return False
    
    return len(stack) == 0
        

print(isValid("[([]){}]"))