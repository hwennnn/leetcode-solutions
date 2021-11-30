class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        
        for x in range(rows):
            for y in range(cols):
                if matrix[x][y] == "1":
                    dp[x][y] = 1
                    res = 1
        
        for x in range(1, rows):
            for y in range(1, cols):
                if matrix[x][y] == "1":
                    z = 1 + min(dp[x][y - 1], dp[x - 1][y - 1], dp[x - 1][y])
                    dp[x][y] = z 
                    res = max(res, z * z)
                else:
                    dp[x][y] = 0
        
        return res
        