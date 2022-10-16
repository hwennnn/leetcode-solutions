class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [c == "0" for c in s]
        m = 0
        
        for i in range(1, len(s)):
            if i >= minJump: m += dp[i - minJump]
            if i > maxJump: m -= dp[i - maxJump - 1]
            
            dp[i] &= m > 0
        
        return dp[-1]