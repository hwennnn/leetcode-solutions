---
id: find-xor-sum-of-all-pairs-bitwise-and
title: Find XOR Sum of All Pairs Bitwise AND
description: Problem Description and Solution for Find XOR Sum of All Pairs Bitwise AND
sidebar_label: 1835. Find XOR Sum of All Pairs Bitwise AND
sidebar_position: 1835
---

# [1835. Find XOR Sum of All Pairs Bitwise AND](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/)

```py title=find-xor-sum-of-all-pairs-bitwise-and.py
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xora = xorb = 0
        
        for num in arr1:
            xora ^= num
        
        for num in arr2:
            xorb ^= num
        
        return xora & xorb
```


