class Solution:
    def calculateMinimumHP(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        dp[rows][cols - 1] = dp[rows - 1][cols] = 1
        
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                need = min(dp[i][j + 1], dp[i + 1][j]) - mat[i][j]
                dp[i][j] = 1 if need <= 0 else need
        
        return dp[0][0]