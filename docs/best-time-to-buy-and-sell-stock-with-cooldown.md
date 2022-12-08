---
id: best-time-to-buy-and-sell-stock-with-cooldown
title: Best Time to Buy and Sell Stock with Cooldown
description: Problem Description and Solution for Best Time to Buy and Sell Stock with Cooldown
sidebar_label: 309. Best Time to Buy and Sell Stock with Cooldown
sidebar_position: 309
---

# [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

```py title=best-time-to-buy-and-sell-stock-with-cooldown.py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        sold, hold, rest = 0, -inf, 0
        
        for x in prices:
            sold, hold, rest = hold + x, max(hold, rest - x), max(rest, sold)
        
        return max(sold, rest)
```


