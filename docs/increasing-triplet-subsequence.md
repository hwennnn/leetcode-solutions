---
id: increasing-triplet-subsequence
title: Increasing Triplet Subsequence
description: Problem Description and Solution for Increasing Triplet Subsequence
sidebar_label: 334. Increasing Triplet Subsequence
sidebar_position: 334
---

# [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/)

```py title=increasing-triplet-subsequence.py
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = inf
        
        for num in nums:
            if num < first:
                first = num
            elif num > first and num < second:
                second = num
            elif num > second:
                return True
        
        return False
```


