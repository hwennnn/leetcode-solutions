class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        
        if low & 1 or high & 1:
            res += 1
        
        return res + (high - low) // 2