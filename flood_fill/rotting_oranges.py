
def orangesRotting(grid):
    
    R, C = len(grid[0]), len(grid)
    minutes = 0
    
    def convert(c,r):
        
        if r < 0 or r >= R or c < 0 or c >= C:
            return 0
        
        # up
        if c + 1 < C:
            if grid[c+1][r] == 2:
                grid[c][r] = 2
                return 1
        # down
        if c - 1 >= 0:
            if grid[c-1][r] == 2:
                grid[c][r] = 2
                return 1
        # right
        if r + 1 < R:
            if grid[c][r+1] == 2:
                grid[c][r] = 2
                return 1
        # left
        if r - 1 >= 0:
            if grid[c][r-1] == 2:
                grid[c][r] = 2
                return 1
    
    prev = None
    current = grid
    
    while prev != grid:
        
        for c in range(0, C):
            for r in range(0, R):
                if grid[c][r] == 1:
                    tmp = current
                    minutes += convert(c, r)
                    current = grid
                    prev = tmp
                    continue
                
        
        
        

    
    
   
                
    print(minutes)
        
            
        
        
            



## 2 = rotting orange
## 1 = orange
## 0 = empty cell

grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]

orangesRotting(grid)

print(grid)