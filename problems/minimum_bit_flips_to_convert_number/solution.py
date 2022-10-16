class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = start ^ goal
        count = 0
        
        while a:
            count += a & 1
            a >>= 1
        
        return count