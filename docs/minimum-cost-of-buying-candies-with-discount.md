---
id: minimum-cost-of-buying-candies-with-discount
title: Minimum Cost of Buying Candies With Discount
description: Problem Description and Solution for Minimum Cost of Buying Candies With Discount
sidebar_label: 2144. Minimum Cost of Buying Candies With Discount
sidebar_position: 2144
---

# [2144. Minimum Cost of Buying Candies With Discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/)

```py title=minimum-cost-of-buying-candies-with-discount.py
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = 1)
        n = len(cost)
        res = 0
        
        for i in range(n // 3):
            res += cost[i * 3] + cost[i * 3 + 1]
        
        for i in range(n % 3):
            res += cost[-i - 1]
        
        return res
```


