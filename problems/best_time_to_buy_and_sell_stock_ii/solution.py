class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        return sum([b-a for a,b in zip(prices,prices[1:]) if b-a > 0])