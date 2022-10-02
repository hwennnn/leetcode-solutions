class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        sold, hold, rest = 0, -inf, 0
        
        for x in prices:
            sold, hold, rest = hold + x, max(hold, rest - x), max(rest, sold)
        
        return max(sold, rest)