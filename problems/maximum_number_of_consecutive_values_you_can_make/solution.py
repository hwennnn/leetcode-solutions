class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        res = 1
        
        for v in sorted(coins):
            if v > res:
                return res
            res += v
        
        return res