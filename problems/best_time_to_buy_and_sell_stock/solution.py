class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = 0
        
        for x in prices:
            buy = min(buy, x)
            sell = max(sell, x - buy)
        
        return sell
        