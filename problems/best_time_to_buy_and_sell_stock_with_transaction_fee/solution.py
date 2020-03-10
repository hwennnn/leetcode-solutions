class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        
        if n < 2: return 0
        
        mini = prices[0] 
        
        ans = 0
        
        for i in range(1,n):
            
            if prices[i] < mini:
                mini = prices[i]
                
            elif prices[i] > mini + fee:
                ans += prices[i] - mini - fee
                mini = prices[i] - fee
                
        return ans