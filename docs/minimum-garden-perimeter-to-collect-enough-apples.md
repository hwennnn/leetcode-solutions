---
id: minimum-garden-perimeter-to-collect-enough-apples
title: Minimum Garden Perimeter to Collect Enough Apples
description: Problem Description and Solution for Minimum Garden Perimeter to Collect Enough Apples
sidebar_label: 1954. Minimum Garden Perimeter to Collect Enough Apples
sidebar_position: 1954
---

# [1954. Minimum Garden Perimeter to Collect Enough Apples](https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/)

```py title=minimum-garden-perimeter-to-collect-enough-apples.py
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        i = 1
        curr = 0
        
        while True:
            first = i + 1
            last = (i * 2) - 1
            
            temp = ((first + last) * (last - first + 1)) // 2
            temp *= 8
            
            temp += (i * 4) + (i * 2) * 4
            curr += temp
            
            if curr >= neededApples: break
            
            i += 1
            
        return i * 8 
```


