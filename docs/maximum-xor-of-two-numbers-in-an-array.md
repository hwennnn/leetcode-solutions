---
id: maximum-xor-of-two-numbers-in-an-array
title: Maximum XOR of Two Numbers in an Array
description: Problem Description and Solution for Maximum XOR of Two Numbers in an Array
sidebar_label: 421. Maximum XOR of Two Numbers in an Array
sidebar_position: 421
---

# [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

```py title=maximum-xor-of-two-numbers-in-an-array.py
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = res = 0
        
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            
            sset = set()
            for num in nums:
                sset.add(num & mask)
            
            desired = res | (1 << i)
            for prefix in sset:
                anotherSum = prefix ^ desired
                
                if anotherSum in sset:
                    res = desired
                    break
            
        return res
```


