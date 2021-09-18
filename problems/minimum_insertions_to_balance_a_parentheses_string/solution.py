class Solution:
    def minInsertions(self, s: str) -> int:
        res = closed = 0
        
        for c in s:
            if c == '(':
                if closed & 1:
                    closed -= 1
                    res += 1
                    
                closed += 2
            else:
                if closed == 0:
                    res += 1
                    closed += 2
                    
                closed -= 1
        
        return res + closed