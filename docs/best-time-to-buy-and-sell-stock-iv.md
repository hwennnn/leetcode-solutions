---
id: best-time-to-buy-and-sell-stock-iv
title: Best Time to Buy and Sell Stock IV
description: Problem Description and Solution for Best Time to Buy and Sell Stock IV
sidebar_label: 188. Best Time to Buy and Sell Stock IV
sidebar_position: 188
---

# [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

```py title=best-time-to-buy-and-sell-stock-iv.py
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if k >= n // 2:
            res = 0
            
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            
            return res
        
        dp = [[0] * (n) for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            tempMax = -prices[0]
            
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tempMax)
                tempMax = max(tempMax, dp[i - 1][j - 1] - prices[j])
        
        return dp[k][n - 1]
```


