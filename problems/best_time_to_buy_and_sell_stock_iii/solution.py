class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * 3
        buy = [prices[0]] * 3
        
        for i in range(1, n):
            for k in range(1, 3):
                buy[k] = min(buy[k], prices[i] - dp[k - 1])
                dp[k] = max(dp[k], prices[i] - buy[k])
        
        return dp[-1]