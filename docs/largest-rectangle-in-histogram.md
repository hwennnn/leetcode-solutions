---
id: largest-rectangle-in-histogram
title: Largest Rectangle in Histogram
description: Problem Description and Solution for Largest Rectangle in Histogram
sidebar_label: 84. Largest Rectangle in Histogram
sidebar_position: 84
---

# [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

```py title=largest-rectangle-in-histogram.py
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0
        
        for i, x in enumerate(heights):
            while x < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)
        
        return res
```


