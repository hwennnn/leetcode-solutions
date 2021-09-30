class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        res = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    res = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                else:
                    dp[i][j] = 0

                res = max(res, dp[i][j])
            
        return res ** 2