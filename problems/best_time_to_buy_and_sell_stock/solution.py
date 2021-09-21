class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = float('inf')
        
        for price in prices:
            buy = min(buy, price)
            res = max(res, price - buy)
        
        return res