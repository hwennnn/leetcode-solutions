class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        equal = (a | b) ^ c
        res = 0
        
        for i in range(31):
            mask = 1 << i
            
            if (mask & equal) > 0:
                res += 2 if (a&mask) == (b&mask) and c & mask == 0 else 1
        
        return res