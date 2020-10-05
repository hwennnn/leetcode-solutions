class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = 1
        while n > x:
            x = x*2 + 1
        
        return x - n