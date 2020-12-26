class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = int(s[0] != "0")
        
        for i in range(2, n+1):
            first = int(s[i-1])
            second = int(s[i-2:i])
            
            if first >= 1 and first <= 9:
                dp[i] += dp[i-1]
            
            if second >= 10 and second <= 26:
                dp[i] += dp[i-2]
        
        
        return dp[n]