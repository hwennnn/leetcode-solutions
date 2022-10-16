class Solution:
    def minSteps(self, S: str, T: str) -> int:
        s = collections.Counter(S)
        t = collections.Counter(T)
        
        for k in s:
            if k in t:
                s[k] = max(0,s[k]-t[k])
        
        res = 0
        for v in s.values():
            res += v
            
        return res