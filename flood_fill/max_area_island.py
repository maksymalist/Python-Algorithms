def max_island(grid):
    
    R, C = len(grid[0]), len(grid)
    visited = [[False for row in range(0,R)] for col in range(0,C)]
    mx = 0
        
    def dfs(r,c):
        
        if r < 0 or r >= len(grid[0]) or c < 0 or c >= len(grid):
            return 0
        
        
        if grid[c][r] == 0 or visited[c][r] == True:
            return 0
        
        visited[c][r] = True
        
        
        return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        
    for i in range(0, C):
        for j in range(0, len(grid[i])):
            print(f"row:{j} col:{i}")
            if grid[i][j] == 1:
                mx = max(dfs(j,i), mx)
    
    return mx
    
    
grid = [[0,0,1,1],
        [1,0,0,1],
        [1,0,0,1]
        ]

print(max_island(grid))