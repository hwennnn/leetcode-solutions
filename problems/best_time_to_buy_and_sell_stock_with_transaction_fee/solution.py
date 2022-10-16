class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        min_buy = prices[0]
        res = 0
        
        for i in range(1, n):
            if prices[i] < min_buy:
                min_buy = prices[i]
            
            elif prices[i] > min_buy + fee:
                res += prices[i] - min_buy - fee
                min_buy = prices[i] - fee
        
        return res