class Solution:
    def numSquares(self, N: int) -> int:
        dp = [inf] * (N + 1)
        dp[0] = 0

        for i in range(1, N + 1):
            curr = inf
            j = 1

            while i - j * j >= 0:
                k = dp[i - j * j] + 1
                if k < curr:
                    curr = k
                j += 1
            
            dp[i] = curr

        return dp[N]