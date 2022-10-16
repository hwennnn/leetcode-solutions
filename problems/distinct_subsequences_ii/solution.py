class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        M = 10 ** 9 + 7
        res = 0
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if s[i] != s[j]:
                    dp[i] += dp[j]
                    dp[i] %= M
            
            res += dp[i]
            res %= M
        
        return res