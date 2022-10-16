class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s,2)
        res = 0
        while n > 1:
            if n & 1:
                n = -(~n)
            else:
                n >>= 1
        
            res += 1
        
        return res