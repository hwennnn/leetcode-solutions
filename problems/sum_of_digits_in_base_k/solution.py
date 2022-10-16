class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        
        while n > 0:
            res += n % k
            n //= k
        
        return res
        