class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        
        full = (1 << n.bit_length()) - 1
        
        return full ^ n