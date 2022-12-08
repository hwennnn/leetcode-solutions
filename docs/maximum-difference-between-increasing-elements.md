---
id: maximum-difference-between-increasing-elements
title: Maximum Difference Between Increasing Elements
description: Problem Description and Solution for Maximum Difference Between Increasing Elements
sidebar_label: 2016. Maximum Difference Between Increasing Elements
sidebar_position: 2016
---

# [2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)

```py title=maximum-difference-between-increasing-elements.py
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, nums[j] - nums[i])
        
        return res
```


