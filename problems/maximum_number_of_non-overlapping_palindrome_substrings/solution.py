class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        N = len(s)
        pal = [[False] * N for _ in range(N)]
        
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                pal[i][j] = s[i] == s[j] and (j - i + 1 < 3 or pal[i + 1][j - 1])
        
        dp = [0] * (N + 1)

        for i in range(N - 1, -1, -1):
            dp[i] = dp[i + 1]
            for j in range(i + k - 1, N):
                if pal[i][j]:
                    dp[i] = max(dp[i], 1 + dp[j + 1])
        
        return dp[0]