---
id: minimum-deletions-to-make-array-divisible
title: Minimum Deletions to Make Array Divisible
description: Problem Description and Solution for Minimum Deletions to Make Array Divisible
sidebar_label: 2344. Minimum Deletions to Make Array Divisible
sidebar_position: 2344
---

# [2344. Minimum Deletions to Make Array Divisible](https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/)

```py title=minimum-deletions-to-make-array-divisible.py
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        
        d = numsDivide[0]
        
        for x in numsDivide:
            d = gcd(d, x)
        
        for i, x in enumerate(nums):
            if d % x == 0:
                return i
        
        return -1
```


