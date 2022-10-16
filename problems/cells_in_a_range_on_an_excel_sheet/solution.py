class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1, _, c2, r2 = s
        res = []
        
        for c in range(ord(c1), ord(c2) + 1):
            for r in range(ord(r1), ord(r2) + 1):
                res.append(chr(c) + chr(r))
        
        return res