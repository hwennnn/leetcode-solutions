class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        
        for x in range(1, min(a, b) + 1):
            if a % x == 0 and b % x == 0:
                res += 1
        
        return res