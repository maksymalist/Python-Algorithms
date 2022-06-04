graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E', 'B'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : ["G"],
    'G' : ['B'],
}

visited = set() # Set to keep track of visited nodes.
queue = set()


def bfs(visited, graph, node, target):

    visited.add(node)
    queue.add(node)
    
    while queue:
        node = queue.pop()

        if node == target:
            return True
            
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.add(neighbour)
                if neighbour == target:
                    return True
    return False


found = bfs(visited, graph, 'A', 'G')

print(found)