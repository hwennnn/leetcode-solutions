---
id: maximum-xor-after-operations
title: Maximum XOR After Operations 
description: Problem Description and Solution for Maximum XOR After Operations 
sidebar_label: 2317. Maximum XOR After Operations 
sidebar_position: 2317
---

# [2317. Maximum XOR After Operations ](https://leetcode.com/problems/maximum-xor-after-operations/)

```py title=maximum-xor-after-operations.py
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        
        for x in nums:
            res |= x
        
        return res
            
```


