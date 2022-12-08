---
id: number-of-smooth-descent-periods-of-a-stock
title: Number of Smooth Descent Periods of a Stock
description: Problem Description and Solution for Number of Smooth Descent Periods of a Stock
sidebar_label: 2110. Number of Smooth Descent Periods of a Stock
sidebar_position: 2110
---

# [2110. Number of Smooth Descent Periods of a Stock](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/)

```py title=number-of-smooth-descent-periods-of-a-stock.py
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        inc = [1] * n
        
        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                inc[i] = inc[i - 1] + 1
        
        return sum(inc)
```


