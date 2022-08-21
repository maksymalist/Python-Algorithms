def bfs(x, y, visited, grid, queue):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return 0
    
    visited.add(queue.add(grid[y][x]))
    queue.add(grid[y][x])
    total = 0
    while visited:
        node = queue.pop()
        
        # up
        if y + 1 < len(grid):
            if grid[y+1][x] == 1:
                if grid[y+1][x] not in visited:
                    queue.add(grid[y+1][x])
                grid[y+1][x] = 2
                total = 1
        # down
        if y - 1 >= 0:
            if grid[y-1][x] == 1:
                if grid[y+1][x] not in visited:
                    queue.add(grid[y+1][x])
                grid[y-1][x] = 2
                total = 1
        # right
        if x + 1 < len(grid[0]):
            if grid[y][x+1] == 1:
                if grid[y+1][x] not in visited:
                    queue.add(grid[y+1][x])
                grid[y][x+1] = 2
                total = 1
        # left
        if x - 1 >= 0:
            if grid[y][x-1] == 1:
                grid[y][x-1] = 2
                total = 1
            
            
    return
            
            
            
        
        
def orangesRotting(grid):
    
    R, C = len(grid[0]), len(grid)
    visited = [[False for cell in range(len(grid[0]))] for row in range(len(grid))]
    minutes = 0
    
    def get_neigbors(x,y):
        neigbors = []
        if x-1 >= 0:
            if grid[y][x-1] == 1:
                neigbors.append([x-1,y])
            
        if x+1 < R:
            if grid[y][x+1] == 1:
                neigbors.append([x+1,y])
            
        if y-1 >= 0:
            if grid[y-1][x] == 1:
                neigbors.append([x,y-1])
            
        if y+1 < C:
            if grid[y+1][x] == 1:
                neigbors.append([x,y+1])
            
        return neigbors
            
            
            
    
    def bfs(x,y):
        
        queue = []
        queue.append([x, y])
        visited[y][x] = True
        mins = 0
        
        while queue:
            
            node = queue.pop()
            
            neigbors = get_neigbors(node[0], node[1])
            for neigbor in neigbors:
                if not visited[neigbor[1]][neigbor[0]]:
                    visited[neigbor[1]][neigbor[0]] = True
                    if grid[neigbor[1]][neigbor[0]] == 1:
                        grid[neigbor[1]][neigbor[0]] = 2
            if neigbors:
                mins += 1
                        
        print(mins)
        print(f"x: {x}, y: {y}")
        for i in grid:
            print(i) 
        print("\n")
        return mins

    for c in range(0, C):
        for r in range(0, R):
            if grid[c][r] == 2:
                minutes += bfs(r, c)
                
    # for c in range(0, C):
    #     for r in range(0, R):
    #         if grid[c][r] == 1:
    #             return -1
               
    return minutes



## 2 = rotting orange
## 1 = orange
## 0 = empty cell

grid = [
        [0,1,1,2,1,0,1,2,0,0],
        [2,1,1,1,1,1,1,1,1,1],
        [1,1,0,0,2,1,0,1,1,1],
        [0,1,1,2,1,0,1,2,0,0],
        [0,1,1,2,1,1,1,2,0,0],
        [1,1,0,0,2,1,0,1,1,1],
        [0,1,1,2,1,1,1,2,0,0],
        [0,1,1,2,1,1,1,2,0,0],
        [1,1,0,0,2,1,0,0,1,1],
        [0,1,1,2,1,0,1,2,0,0],
        ]
    
print(orangesRotting(grid))