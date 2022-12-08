---
id: reducing-dishes
title: Reducing Dishes
description: Problem Description and Solution for Reducing Dishes
sidebar_label: 1402. Reducing Dishes
sidebar_position: 1402
---

# [1402. Reducing Dishes](https://leetcode.com/problems/reducing-dishes/)

```py title=reducing-dishes.py
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        
        res = m = c = 0
        
        for i in range(n - 1, -1, -1):
            m += c + satisfaction[i]
            c += satisfaction[i]
            res = max(res, m)
        
        return res
```


