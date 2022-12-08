---
id: single-number
title: Single Number
description: Problem Description and Solution for Single Number
sidebar_label: 136. Single Number
sidebar_position: 136
---

# [136. Single Number](https://leetcode.com/problems/single-number/)

```py title=single-number.py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for x in nums:
            res ^= x
        
        return res
```


