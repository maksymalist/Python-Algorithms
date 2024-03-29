class Solution:
    
    def multiply_matrices(self, mat1, mat2):
        
        for y in range(len(mat1)):
            for x in range(len(mat1[0])):
                if mat2[y][x]:
                    mat1[y][x] = mat1[y][x] * mat2[y][x]
                
        return mat1
    


mat_1 = [
    [1,2,3,4,45,5,7,8],
    [1,2,3,4,45,5,7,8],
    [1,2,3,4,45,5,7,8],
    [1,2,3,4,45,5,7,8],
    [1,2,3,4,45,5,7,8],
    [1,2,3,4,45,5,7,8],
    [1,2,3,4,45,5,7,8],
    [1,2,3,4,45,5,7,8]
]

mat_2 = [
    [5,2,3,4,45,5,7,8],
    [7,2,3,4,45,5,7,8],
    [4,2,3,4,45,5,7,8],
    [2,2,3,4,45,5,7,8],
    [7,2,3,4,45,5,7,8],
    [9,2,3,4,45,5,7,8],
    [7,2,3,4,45,5,7,8],
    [2,2,3,4,45,5,7,8]
]
    
    
for i in Solution().multiply_matrices(mat_1, mat_2):
    print(i)