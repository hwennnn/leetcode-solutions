---
id: best-time-to-buy-and-sell-stock-ii
title: Best Time to Buy and Sell Stock II
description: Problem Description and Solution for Best Time to Buy and Sell Stock II
sidebar_label: 122. Best Time to Buy and Sell Stock II
sidebar_position: 122
---

# [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

```py title=best-time-to-buy-and-sell-stock-ii.py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        
        for i in range(1, n):
            dp[i] = max(dp[i - 1], dp[i - 1] + prices[i] - prices[i - 1])
        
        return dp[-1]
```


