---
id: two-furthest-houses-with-different-colors
title: Two Furthest Houses With Different Colors
description: Problem Description and Solution for Two Furthest Houses With Different Colors
sidebar_label: 2078. Two Furthest Houses With Different Colors
sidebar_position: 2078
---

# [2078. Two Furthest Houses With Different Colors](https://leetcode.com/problems/two-furthest-houses-with-different-colors/)

```py title=two-furthest-houses-with-different-colors.py
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        n = len(colors)
        
        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    res = max(res, j - i)
        
        return res
            
```


