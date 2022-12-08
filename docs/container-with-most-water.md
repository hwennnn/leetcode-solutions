---
id: container-with-most-water
title: Container With Most Water
description: Problem Description and Solution for Container With Most Water
sidebar_label: 11. Container With Most Water
sidebar_position: 11
---

# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

```py title=container-with-most-water.py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        left, right = 0, n - 1
        
        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return res
```


