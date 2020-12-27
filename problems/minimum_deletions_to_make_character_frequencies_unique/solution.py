class Solution:
    def minDeletions(self, S: str) -> int:
        c = collections.Counter(S)
        res = 0
        s = set()
        
        for ch in c.values():
            
            while ch > 0 and ch in s:
                res += 1
                ch -= 1
            
            if ch > 0: s.add(ch)
        
        return res