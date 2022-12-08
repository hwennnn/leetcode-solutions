---
id: bitwise-xor-of-all-pairings
title: Bitwise XOR of All Pairings
description: Problem Description and Solution for Bitwise XOR of All Pairings
sidebar_label: 2425. Bitwise XOR of All Pairings
sidebar_position: 2425
---

# [2425. Bitwise XOR of All Pairings](https://leetcode.com/problems/bitwise-xor-of-all-pairings/)

```py title=bitwise-xor-of-all-pairings.py
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        xor = 0
        if n2 % 2 != 0:
            for x in nums1:
                xor ^= x
        
        if n1 % 2 != 0:
            for x in nums2:
                xor ^= x
        
        return xor
```


