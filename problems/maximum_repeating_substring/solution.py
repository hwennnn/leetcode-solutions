class Solution:
    def maxRepeating(self, seq: str, w: str) -> int:
        
        res = 0
        s = set()
        times = len(seq) // len(w)
        p = [w * i for i in range(1, times+1)]

        for c in p:
            if c not in s and c in seq:
                s.add(c)
                res += 1
        
        return res