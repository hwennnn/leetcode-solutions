---
id: find-positive-integer-solution-for-a-given-equation
title: Find Positive Integer Solution for a Given Equation
description: Problem Description and Solution for Find Positive Integer Solution for a Given Equation
sidebar_label: 1237. Find Positive Integer Solution for a Given Equation
sidebar_position: 1237
---

# [1237. Find Positive Integer Solution for a Given Equation](https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/)

```py title=find-positive-integer-solution-for-a-given-equation.py
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        y = 1000
        res = []        
        for x in range(1,1000):
            while y > 1 and customfunction.f(x,y) > z:
                y -= 1
            
            if customfunction.f(x,y) == z:
                res.append([x,y])
        
        return res
```


