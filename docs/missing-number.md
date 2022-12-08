---
id: missing-number
title: Missing Number
description: Problem Description and Solution for Missing Number
sidebar_label: 268. Missing Number
sidebar_position: 268
---

# [268. Missing Number](https://leetcode.com/problems/missing-number/)

```py title=missing-number.py
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        
        return total - sum(nums)
```


