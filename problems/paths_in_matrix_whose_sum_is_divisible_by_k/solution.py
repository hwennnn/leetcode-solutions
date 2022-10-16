M = 10 ** 9 + 7

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(rows):
            for j in range(cols):
                for kk in range(k):
                    dp[i][j][kk] %= M
                    if i + 1 < rows:
                        dp[i + 1][j][(grid[i + 1][j] + kk) % k] += dp[i][j][kk]
                    if j + 1 < cols:
                        dp[i][j + 1][(grid[i][j + 1] + kk) % k] += dp[i][j][kk]
        
        return dp[rows - 1][cols - 1][0]