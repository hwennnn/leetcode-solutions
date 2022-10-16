class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x = y = 0
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j
        
        left, right = y - 1, y + 1
        top, bottom = x - 1, x + 1
        res = 0
        
        while left >= 0:
            if board[x][left] == ".":
                left -= 1
            elif board[x][left] == "B":
                break
            elif board[x][left] == "p":
                res += 1
                break
        
        while right < 8:
            if board[x][right] == ".":
                right += 1
            elif board[x][right] == "B":
                break
            elif board[x][right] == "p":
                res += 1
                break
        
        while top >= 0:
            if board[top][y] == ".":
                top -= 1
            elif board[top][y] == "B":
                break
            elif board[top][y] == "p":
                res += 1
                break
        
        while bottom < 8:
            if board[bottom][y] == ".":
                bottom += 1
            elif board[bottom][y] == "B":
                break
            elif board[bottom][y] == "p":
                res += 1
                break
        
        return res
        
        
                
        