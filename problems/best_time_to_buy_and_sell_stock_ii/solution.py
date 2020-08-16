class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        if (n < 2): return 0
        
        dp = [None] * n
        dp[0] = 0
        
        for i in range(1,n):
            dp[i] = max(dp[i-1], dp[i-1] + prices[i] - prices[i-1])
                
        return dp[-1]