import stat
from turtle import down


mat = [
    [1,0,0,0,0,0],
    [0,1,0,1,1,1],
    [0,0,1,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,1,1,0],
    [1,0,0,0,0,1]
]

def solution(mat):
    
    visited = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
    
    
    def dfs(x,y):
        
        if visited[y][x] == 1 or mat[y][x] == 0:
            return
            
        
        visited[y][x] = 1
    

        if x > 0:
            dfs(x-1,y)
        if x < len(mat[0])-1:
            dfs(x+1,y)
        if y > 0:
            dfs(x,y-1)
        if y < len(mat)-1:
            dfs(x,y+1)
        
        
        
            
        
    
    for y, row in enumerate(mat):
        for x, val in enumerate(row):
            # check if part of perimeter
            if val == 1 and y == 0 or y == len(mat) - 1 or x == 0 or x == len(mat[0]) - 1:
                dfs(x, y)
                    
    return visited
                
                
    

for i in solution(mat):
    print(i)