
def cloneGraph(node):
    
    def getNeighborsVals():
        out = []
        for n in node.neighbors:
            out.append(nei)
            
    
    visited = set()
    adj_list = []
    def dfs(node, vis, adj_list):
        
        if node not in vis:
            vis.add(node)
            print(node.val)
            adj_list.append(node.neighbors)
            
            for neighbor in node.neighbors:
                dfs(neighbor, vis, adj_list)
        
        
    
    
                        
    dfs(node, visited, adj_list)
    print(adj_list)
    

