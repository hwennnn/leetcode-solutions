class Solution:
    def minCut(self, s: str) -> int:
        if len(s) == 1: return 0
        
        n = len(s)
        dp = list(range(n))
        
        for mid in range(1, n):
            
            start = end = mid
            while start >= 0 and end < n and s[start] == s[end]:
                cut = 0 if start == 0 else dp[start - 1] + 1
                dp[end] = min(dp[end], cut)
                start -= 1
                end += 1
            
            start, end = mid - 1, mid
            while start >= 0 and end < n and s[start] == s[end]:
                cut = 0 if start == 0 else dp[start - 1] + 1
                dp[end] = min(dp[end], cut)
                start -= 1
                end += 1
        
        return dp[-1]