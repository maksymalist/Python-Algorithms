class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        R, C = len(board[0]), len(board)
        safe = [[False for x in board[0]] for y in board]
            
        def fill(x, y):
            if x < 0 or y < 0 or x >= R or y >= C:
                return
            
            if board[y][x] == "X" or safe[y][x]:
                return
            
            safe[y][x] = True  

            
            fill(x+1, y)
            fill(x-1, y)
            fill(x, y+1)
            fill(x, y-1)
        
        for x in range(R):
            
            if board[0][x] == "O":
                fill(x, 0)
            
            if board[-1][x] == "O":
                fill(x, C-1)
            
        
        for y in range(C):
            
            if board[y][0] == "O":
                fill(0, y)
                    
            if board[y][-1] == "O":
                fill(R-1, y)
                
        for y in range(C):
            for x in range(R):
                if not safe[y][x]:
                    board[y][x] = "X"