---
id: best-time-to-buy-and-sell-stock-iii
title: Best Time to Buy and Sell Stock III
description: Problem Description and Solution for Best Time to Buy and Sell Stock III
sidebar_label: 123. Best Time to Buy and Sell Stock III
sidebar_position: 123
---

# [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

```py title=best-time-to-buy-and-sell-stock-iii.py
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
```


