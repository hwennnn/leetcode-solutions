---
id: single-number-ii
title: Single Number II
description: Problem Description and Solution for Single Number II
sidebar_label: 137. Single Number II
sidebar_position: 137
---

# [137. Single Number II](https://leetcode.com/problems/single-number-ii/)

```py title=single-number-ii.py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        
        for x in nums:
            ones = (ones ^ x) & ~twos
            twos = (twos ^ x) & ~ones
        
        return ones
```


