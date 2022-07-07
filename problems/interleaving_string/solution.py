class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)
        
        if n + m != k: return False
        
        @cache
        def go(a, b):
            if a + b == k: 
                return True
            
            res = False
            
            if a < n and s1[a] == s3[a + b]:
                res |= go(a + 1, b)
            
            if b < m and s2[b] == s3[a + b]:
                res |= go(a, b + 1)
            
            return res
        
        return go(0, 0)