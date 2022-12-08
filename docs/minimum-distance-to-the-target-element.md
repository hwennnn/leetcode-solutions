---
id: minimum-distance-to-the-target-element
title: Minimum Distance to the Target Element
description: Problem Description and Solution for Minimum Distance to the Target Element
sidebar_label: 1848. Minimum Distance to the Target Element
sidebar_position: 1848
---

# [1848. Minimum Distance to the Target Element](https://leetcode.com/problems/minimum-distance-to-the-target-element/)

```py title=minimum-distance-to-the-target-element.py
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min([abs(i - start) for i in range(len(nums)) if nums[i] == target])
```


