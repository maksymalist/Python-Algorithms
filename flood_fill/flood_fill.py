grid = [[1,1,1],[1,1,0],[1,0,1]]


def flood_fill(r, c, old, new):
    if c < 0 or r < 0 or c >= len(grid) or r >= len(grid[0]):
        return
    
    if grid[c][r] != old:
        return
    
    grid[c][r] = new
    
    flood_fill(r+1,c,old, new)
    flood_fill(r-1,c,old, new)
    flood_fill(r,c+1,old, new)
    flood_fill(r,c-1,old, new)
    
    
flood_fill(0,0,1,2)
print(grid)