class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        res = 0
        
        for x in s:
            v = ord(x) - ord("a")
            dp[v] += 1
            
            for z in range(max(0, v - k), min(25, v + k) + 1):
                if v != z:
                    dp[v] = max(dp[v], dp[z] + 1)
            
            res = max(res, dp[v])
        
        return res