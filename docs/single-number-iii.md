---
id: single-number-iii
title: Single Number III
description: Problem Description and Solution for Single Number III
sidebar_label: 260. Single Number III
sidebar_position: 260
---

# [260. Single Number III](https://leetcode.com/problems/single-number-iii/)

```py title=single-number-iii.py
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bit = 0
        res = [0, 0]
        
        for x in nums:
            bit ^= x
        
        bit &= -bit
        
        for x in nums:
            if bit & x == 0:
                res[0] ^= x
            else:
                res[1] ^= x
        
        return res
```


