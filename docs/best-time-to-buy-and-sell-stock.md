---
id: best-time-to-buy-and-sell-stock
title: Best Time to Buy and Sell Stock
description: Problem Description and Solution for Best Time to Buy and Sell Stock
sidebar_label: 121. Best Time to Buy and Sell Stock
sidebar_position: 121
---

# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```py title=best-time-to-buy-and-sell-stock.py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = 0
        
        for x in prices:
            buy = min(buy, x)
            sell = max(sell, x - buy)
        
        return sell
        
```


