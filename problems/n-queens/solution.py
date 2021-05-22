class Solution:
    def solveNQueens(self, n):
        
        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in b])
                return
            for c in range(n):
                if isValid(r, c):
                    b[r][c] = 'Q'
                    dfs(r + 1)      # fill row by row
                    b[r][c] = '.'
        
        def isValid(r, c):
            for i in range(r):
                for j in range(n):
                    if b[i][j] == 'Q' and (c == j or        # same column
                                           i+j == r+c or    # 45 degree line
                                           i-j == r-c):     # 135 degree line
                        return False
            return True
                        
        
        b = [['.'] * n for _ in range(n)]
        res = []
        dfs(0)      # start from row 0
        
        return res