class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = "#"

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        def dfs(root):
            if root:
                if root.val == find_val:
                    return True
                
                return dfs(root.right) or dfs(root.left)
                
        if dfs(self.root): return True
        return False
    
    
    def connect(self):
        if not self.root:
            return self.root
        
        self.root.next = "#"
        def dfs(node):
            if node:
                
                if node.right:
                    if node.next != "#":
                        node.right.next = node.next.left 
                    
                if node.left and node.right:
                    node.left.next = node.right
                    
                dfs(node.left)
                dfs(node.right)
                
        dfs(self.root)
                
        
    

    def print_tree(self):
        res = []
        def dfs(root):
            if root:
                next = "#"
                if root.next != "#":
                    next = root.next.val
                res.append(str(root.val) + f"({next})")
                dfs(root.right)
                dfs(root.left)
                
        dfs(self.root)
        return "-".join(res)


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.right = Node(7)
tree.root.right.left = Node(6)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(69))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())

tree.connect()

print(tree.print_tree())
