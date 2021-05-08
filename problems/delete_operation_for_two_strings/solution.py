class Solution:
    def minDistance(self, w1, w2):

        m, n = len(w1), len(w2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                if w1[i] == w2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        lcs = dp[-1][-1]

        return m + n - (2 * lcs)