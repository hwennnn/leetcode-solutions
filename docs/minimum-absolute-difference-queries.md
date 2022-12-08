---
id: minimum-absolute-difference-queries
title: Minimum Absolute Difference Queries
description: Problem Description and Solution for Minimum Absolute Difference Queries
sidebar_label: 1906. Minimum Absolute Difference Queries
sidebar_position: 1906
---

# [1906. Minimum Absolute Difference Queries](https://leetcode.com/problems/minimum-absolute-difference-queries/)

```py title=minimum-absolute-difference-queries.py
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        dp = [[0] * (max(nums) + 1)]
        
        for i, x in enumerate(nums):
            t = dp[-1][:]
            t[x] += 1
            dp.append(t)
        
        res = []
        for start, end in queries:
            A = [i for i, (a,b) in enumerate(zip(dp[start], dp[end + 1])) if a != b]
            res.append(min([b - a for a,b in zip(A, A[1:])] or [-1]))
            
        return res
```


