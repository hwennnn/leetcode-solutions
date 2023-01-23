class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        sign = 1
        
        for x in map(int, str(n)):
            res += sign * x
            sign *= -1
        
        return res