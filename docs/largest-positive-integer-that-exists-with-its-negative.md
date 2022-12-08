---
id: largest-positive-integer-that-exists-with-its-negative
title: Largest Positive Integer That Exists With Its Negative
description: Problem Description and Solution for Largest Positive Integer That Exists With Its Negative
sidebar_label: 2441. Largest Positive Integer That Exists With Its Negative
sidebar_position: 2441
---

# [2441. Largest Positive Integer That Exists With Its Negative](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/)

```py title=largest-positive-integer-that-exists-with-its-negative.py
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        
        for x in range(1000, 0, -1):
            if x in s and -x in s:
                return x
        
        return -1
```


