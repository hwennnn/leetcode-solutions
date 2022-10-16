class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        M = 10 ** 9 + 7
        
        return (pow(2 ** p - 2, 2 ** (p - 1) - 1, M) * (2 ** p - 1)) % M