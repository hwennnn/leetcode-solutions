class Solution:
    def minDeletions(self, S: str) -> int:
        c = Counter(S)
        s = set()
        res = 0
        
        for v in c.values():
            t = v
            
            while t in s:
                res += 1
                t -= 1
            
            if t != 0:
                s.add(t)
            
        return res
        