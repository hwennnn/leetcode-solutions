---
id: best-time-to-buy-and-sell-stock-with-transaction-fee
title: Best Time to Buy and Sell Stock with Transaction Fee
description: Problem Description and Solution for Best Time to Buy and Sell Stock with Transaction Fee
sidebar_label: 714. Best Time to Buy and Sell Stock with Transaction Fee
sidebar_position: 714
---

# [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

```py title=best-time-to-buy-and-sell-stock-with-transaction-fee.py
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
```


