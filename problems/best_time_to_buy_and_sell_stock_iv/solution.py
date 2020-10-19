class Solution:
    def maxProfit(self, k, prices):
        if k >= int(len(prices) / 2):
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res
        if len(prices) == 0 or k == 0:
            return 0
        dp = [[[0,0] for i in range(len(prices)+1)] for j in range(k+1)]
        for i in range(k+1):
            dp[i][0][0] = -prices[0]
        for i in range(1,k+1):
            for p in range(1,len(prices)+1):
                dp[i][p][0] = max(dp[i][p-1][0], dp[i-1][p-1][1] - prices[p-1])
                dp[i][p][1] = max(dp[i][p-1][1], dp[i][p-1][0] + prices[p-1], 0)   

        return dp[-1][-1][-1]
