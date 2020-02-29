class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy,sold = float('inf'),0
        
        for price in prices:
            buy = min(price,buy)
            profit = price - buy
            sold = max(sold,profit)
            
        return sold