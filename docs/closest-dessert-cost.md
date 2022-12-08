---
id: closest-dessert-cost
title: Closest Dessert Cost
description: Problem Description and Solution for Closest Dessert Cost
sidebar_label: 1774. Closest Dessert Cost
sidebar_position: 1774
---

# [1774. Closest Dessert Cost](https://leetcode.com/problems/closest-dessert-cost/)

```py title=closest-dessert-cost.py
class Solution:
    res = float('inf')
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n = len(toppingCosts)
        
        def helper(current, index):
            
            if abs(target - current) < abs(target - self.res) or (abs(target - current) == abs(target - self.res) and current < self.res):
                self.res = current
            
            if index == n or current > target: return
            
            helper(current, index + 1)
            helper(current + toppingCosts[index], index + 1)
            helper(current + toppingCosts[index] * 2, index + 1)
            
        for base in baseCosts:
            helper(base, 0)
        
        return self.res
```


