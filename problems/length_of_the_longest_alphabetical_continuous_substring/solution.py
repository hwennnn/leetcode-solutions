class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        N = len(s)
        res = length = 1
        
        def f(x):
            return ord(x) - ord("a")
        
        prev = f(s[0])
        
        for i in range(1, N):
            curr = f(s[i])
            
            if prev + 1 == curr:
                length += 1
                res = max(res, length)
            else:
                length = 1
            
            prev = curr
        
        return res