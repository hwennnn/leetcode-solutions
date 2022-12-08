---
id: maximum-population-year
title: Maximum Population Year
description: Problem Description and Solution for Maximum Population Year
sidebar_label: 1854. Maximum Population Year
sidebar_position: 1854
---

# [1854. Maximum Population Year](https://leetcode.com/problems/maximum-population-year/)

```py title=maximum-population-year.py
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        people = [0] * 2051
        
        for b,d in logs:
            people[b] += 1
            people[d] -= 1

        for i in range(1, 2051):
            people[i] += people[i - 1]
            
        res = 0
        mmax = float('-inf')
        for i,x in enumerate(people):
            if x > mmax:
                res = i
                mmax = x
        
        return res
```


