class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    

    def print_tree(self):
        res = []
        def dfs(root):
            if root:
                res.append(str(root.value))
                dfs(root.right)
                dfs(root.left)

def rob(nums):
    

    def find_path(left, curr, right, options, tt):
        if len(options) <= 0:
            return tt
        
        print(left, curr, right)
        
        clone = options[:]
        
        if left and left > 0:
            clone.pop(left)
            
        if right and right < len(options):
            clone.pop(right)
                
        options.pop(curr)
        
        most = 0

        for i in range(len(clone)):
            if options[i] > most:
                most = options[i]
        tt += most
        next = i + 1
        return find_path(next-1, next, next+1, options, tt)
                

    mx = 0
    for i in range(len(nums)):
        clone = nums[:]
        left = i - 1
        right = i + 1
        
        if left <0:
            left = None
        if right >= len(nums):
            right = None
            
        find_path(left, i, right, clone, nums[i])



    return mx

print(rob([2,7,9,3,1]))