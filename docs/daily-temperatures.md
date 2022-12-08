---
id: daily-temperatures
title: Daily Temperatures
description: Problem Description and Solution for Daily Temperatures
sidebar_label: 739. Daily Temperatures
sidebar_position: 739
---

# [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

```py title=daily-temperatures.py
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        stack = []
        res = [0] * n
        
        for i, x in enumerate(T):
            while stack and x > T[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            
            stack.append(i)
        
        return res
        
        
```


