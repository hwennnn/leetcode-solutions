class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = i
            
            for j in range(i - 1, 1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + (i // j)
                    break
        
        return dp[n]