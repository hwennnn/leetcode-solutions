class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            mmin = float('inf')
            j = 1
            
            while i - j * j >= 0:
                mmin = min(mmin, dp[i - j * j] + 1)
                j += 1
                
            dp[i] = mmin

        return dp[n]