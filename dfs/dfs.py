# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E', 'B', 'A'],
    'C' : ['F'],
    'D' : ['F'],
    'E' : ['F'],
    'F' : ['G'],
    'G' : ['B'],
}

visited = set() # Set to keep track of visited nodes
def dfs(visited, graph, node, target):
    
    if not graph.get(node):
        return False
    
    if node == target:
        return True
    
    if node not in visited:
        visited.add(node)
        
        for neigbor in graph[node]:
            if dfs(visited, graph, neigbor, target):
                return True
            
    return False
# Driver Code
found = dfs(visited, graph, 'Ds', 'A')

print(found)