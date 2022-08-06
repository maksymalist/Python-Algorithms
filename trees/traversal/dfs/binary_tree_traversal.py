class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        def dfs(root):
            if root:
                if root.value == find_val:
                    return True
                
                return dfs(root.right) or dfs(root.left)
                
        if dfs(self.root): return True
        return False
        
    

    def print_tree(self):
        res = []
        def dfs(root):
            if root:
                res.append(str(root.value))
                dfs(root.right)
                dfs(root.left)
                
        dfs(self.root)
        return "-".join(res)

    def preorder_search(self, start, find_val):
        pass

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(33))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())