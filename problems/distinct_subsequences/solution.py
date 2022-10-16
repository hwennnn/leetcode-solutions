class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for j in range(m + 1):
            dp[0][j] = 1
        
        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = dp[i + 1][j]
                if t[i] == s[j]:
                    dp[i + 1][j + 1] += dp[i][j]
        
        return dp[n][m]