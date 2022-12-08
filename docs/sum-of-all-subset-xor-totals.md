---
id: sum-of-all-subset-xor-totals
title: Sum of All Subset XOR Totals
description: Problem Description and Solution for Sum of All Subset XOR Totals
sidebar_label: 1863. Sum of All Subset XOR Totals
sidebar_position: 1863
---

# [1863. Sum of All Subset XOR Totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)

```py title=sum-of-all-subset-xor-totals.py
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for mask in range(1 << n):
            count = 0
            for j in range(n):
                if mask >> j & 1:
                    count ^= nums[j]
                
            res += count
        
        return res
```


