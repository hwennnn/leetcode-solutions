---
id: number-of-ways-to-buy-pens-and-pencils
title: Number of Ways to Buy Pens and Pencils
description: Problem Description and Solution for Number of Ways to Buy Pens and Pencils
sidebar_label: 2240. Number of Ways to Buy Pens and Pencils
sidebar_position: 2240
---

# [2240. Number of Ways to Buy Pens and Pencils](https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/)

```py title=number-of-ways-to-buy-pens-and-pencils.py
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        
        if cost2 > cost1:
            cost1, cost2 = cost2, cost1
        
        res = 0
        
        for buy in range(total // cost1 + 1):
            curr = total - (buy * cost1)
            res += (curr // cost2) + 1
        
        return res
```


