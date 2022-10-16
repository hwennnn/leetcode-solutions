class Solution:
    def concatenatedBinary(self, n: int) -> int:
        M = 10 ** 9 + 7
        
        total = 0
        for x in range(1, n + 1):
            total *= pow(2, x.bit_length())
            total += x
            total %= M
        
        return total