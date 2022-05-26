class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n > 0:
            if n & 1:
                res += 1
            n >>= 1
        
        return res