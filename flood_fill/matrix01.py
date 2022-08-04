def updateMatrix(mat):
    
    R, C = len(mat[0]), len(mat)
        
    def dfs(r,c):
        
        if r < 0 or r >= len(mat[0]) -1 or c < 0 or c >= len(mat)-1:
            return 0
        
        
        print(r, c)
        
        
        if mat[c][r] != 1:
            return 0
        
        neighbors = 4
        
        if mat[c][r+1] == 1:
            neighbors -= 1
            
        if mat[c+1][r] == 1:
            neighbors -= 1
            
        if mat[c-1][r] == 1:
            neighbors -= 1
            
        if mat[c][r-1] == 1:
            neighbors -= 1
        
        if neighbors == 0:
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        else:
            return 1
            
    for y in range(0, C):
        for x in range(0, R):
            if mat[y][x] > 1:
                mat[y][x] = dfs(x,y)
        
    return mat

print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))