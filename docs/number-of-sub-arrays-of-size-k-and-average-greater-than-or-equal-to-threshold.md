---
id: number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
title: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
description: Problem Description and Solution for Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
sidebar_label: 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
sidebar_position: 1343
---

# [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

```py title=number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold.py
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        prefix = [0] * (n+1)
        res = 0
        
        for i,num in enumerate(arr):
            prefix[i+1] += prefix[i] + num
        
        for i in range(n-k+1):
            if (prefix[i+k] - prefix[i]) >= threshold * k:
                res += 1
        
        return res
```


