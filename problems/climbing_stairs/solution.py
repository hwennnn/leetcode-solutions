class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 4: return n
        
        dp = [0,1,2,3]
        
        for i in range(4,n+1):
            dp.append(dp[i-1] + dp[i-2])
            
        return dp[-1]
        