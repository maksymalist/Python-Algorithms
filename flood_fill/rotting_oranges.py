
def orangesRotting(grid):
    
    R, C = len(grid[0]), len(grid)
    visited = [[False for i in range(R) ] for j in range(C)]
    minutes = 0
    
    def convert(c,r):
        
        if r < 0 or r >= R or c < 0 or c >= C:
            return 0
        
        if visited[c][r]:
            return 0
        
        total = 0
        
        # up
        if c + 1 < C:
            if grid[c+1][r] == 1:
                grid[c+1][r] = 2
                total = 1
        # down
        if c - 1 >= 0:
            if grid[c-1][r] == 1:
                grid[c-1][r] = 2
                total = 1
        # right
        if r + 1 < R:
            if grid[c][r+1] == 1:
                grid[c][r+1] = 2
                total = 1
        # left
        if r - 1 >= 0:
            if grid[c][r-1] == 1:
                grid[c][r-1] = 2
                total = 1
            
        return total
    

    for c in range(0, C):
        for r in range(0, R):
            if grid[c][r] == 2:
                minutes += convert(c, r)
                
    for c in range(0, C):
        for r in range(0, R):
            if grid[c][r] == 1:
                minutes = -1
    
    print(grid)
    return minutes



## 2 = rotting orange
## 1 = orange
## 0 = empty cell

grid = [[2,1,1],
        [0,1,1],
        [1,0,1]]

print(orangesRotting(grid))