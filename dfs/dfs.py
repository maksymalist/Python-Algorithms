# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E', 'B'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
    'G' : ['B'],
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node, target):
    print(node)
    if node == target:
        return True
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour, target):
                return True
    return False

# Driver Code
found = dfs(visited, graph, 'A', 'D')

print(found)