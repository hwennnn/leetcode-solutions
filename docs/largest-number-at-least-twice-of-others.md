---
id: largest-number-at-least-twice-of-others
title: Largest Number At Least Twice of Others
description: Problem Description and Solution for Largest Number At Least Twice of Others
sidebar_label: 747. Largest Number At Least Twice of Others
sidebar_position: 747
---

# [747. Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/)

```py title=largest-number-at-least-twice-of-others.py
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        highestindex, h1, h2 = 0, -1, -1
        
        for i,num in enumerate(nums):
            if num > h1:
                h2 = h1
                h1 = num
                highestindex = i
                
            elif num > h2 and num < h1:
                h2 = num
                
        return highestindex if h1 >= h2*2 else -1
```


