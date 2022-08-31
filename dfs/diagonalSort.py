g = [[93,49,54,89,100,90,63,28,46,67],
 [24,97,48,73,62,32,44,100,24,79],
 [81,65,45,14,79,86,45,53,68,83],
 [29,83,12,90,39,37,4,91,62,43],
 [87,19,42,54,30,31,92,24,44,43],
 [97,63,90,89,38,73,60,31,20,91],
 [93,36,83,50,27,89,27,47,80,5],
 [8,99,39,62,24,25,50,58,67,20],
 [84,42,21,55,92,48,84,6,79,11]]


g2 = [[27,11,20,4,32,43,43,24,46,67],[6,30,14,31,5,44,44,63,28,79],[25,12,45,31,37,20,45,53,68,83],[19,27,24,58,39,54,24,91,62,100],[62,24,42,38,73,47,73,62,91,90],[36,63,29,81,50,79,48,79,86,100],[21,39,83,48,83,54,90,49,80,89],[8,93,55,87,50,84,65,93,60,92],[84,42,99,97,92,90,89,89,97,67]]

g3 = []

class Solution:
    def diagonalSort(self, mat):
        
        R,C = len(mat[0]), len(mat)
        
        def replace_old(r,c, new):
            
            d_index = c-r
            if d_index < 0:
                d_index = d_index*-1
                
            span = len(mat[c])-d_index-1
            
            for i in range(len(new)):
                mat[c+i][r+i] = new[i]
                
                
        
        def sort_diag(x, y):
            
            diag = []
            
            def dfs(r,c):
                if r < 0 or c < 0 or r >= R or c >= C:
                    return
                if r == c:
                    print(mat[c][r])
                diag.append(mat[c][r])
                dfs(r+1,c+1)
            
            dfs(x, y)
            sorted_diag = sorted(diag)
            print(sorted_diag)
            replace_old(x, y, sorted_diag)
        
        for y in range(C):
            sort_diag(0, y)
            
        for x in range(1,R):
            sort_diag(x, 0)
            
        for y in range(len(g)):
            row = []
            for x in range(len(g[y])):
                if g[y][x] == g2[y][x]:
                    row.append("🟩")
                else:
                    row.append("🟥")
            g3.append(row)
            
        for i in g3:
            print(i)
            
        return mat
    
    
print(Solution().diagonalSort(g))


# g1=[[27,11,20,4,32,43,43,24,46,67],[6,30,14,31,5,44,44,63,28,79],[25,12,45,31,37,20,45,53,68,83],[19,27,24,58,39,54,24,91,62,43],[62,24,42,38,73,47,73,62,91,43],[36,63,29,81,50,79,48,79,86,91],[21,39,83,48,83,54,90,49,80,5],[8,93,55,87,50,84,65,93,60,20],[84,42,99,97,92,90,89,89,97,11]]

# g2 = [[27,11,20,4,32,43,43,24,46,67],[6,30,14,31,5,44,44,63,28,79],[25,12,45,31,37,20,45,53,68,83],[19,27,24,58,39,54,24,91,62,100],[62,24,42,38,73,47,73,62,91,90],[36,63,29,81,50,79,48,79,86,100],[21,39,83,48,83,54,90,49,80,89],[8,93,55,87,50,84,65,93,60,92],[84,42,99,97,92,90,89,89,97,67]]

# g3 = []

# for y in range(len(g1)):
#     row = []
#     for x in range(len(g1[y])):
#         if g1[y][x] == g2[y][x]:
#             row.append("🟩")
#         else:
#             row.append("🟥")
#     g3.append(row)
    
# for i in g3:
#     print(i)