class Solution:
    def maximumEvenSplit(self, s: int) -> List[int]:
        if s & 1: return []
        
        res = []
        x = 2
        
        while x <= s:
            res.append(x)
            s -= x
            x += 2
            
        res[-1] += s
        
        return res