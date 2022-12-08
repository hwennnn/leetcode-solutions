---
id: distribute-repeating-integers
title: Distribute Repeating Integers
description: Problem Description and Solution for Distribute Repeating Integers
sidebar_label: 1655. Distribute Repeating Integers
sidebar_position: 1655
---

# [1655. Distribute Repeating Integers](https://leetcode.com/problems/distribute-repeating-integers/)

```py title=distribute-repeating-integers.py
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        counter = sorted(Counter(nums).values())
        n, m = len(counter), len(quantity)
        
        mask_sum = defaultdict(int)
        
        for mask in range(1 << m):
            for j in range(m):
                if (1 << j) & mask > 0:
                    mask_sum[mask] += quantity[j]

        @cache
        def go(index, mask):
            if mask == 0: return True
            
            if index == n: return False
            
            submask = mask
            
            while submask:
                if counter[index] >= mask_sum[submask] and go(index + 1, submask ^ mask):
                    return True
                
                submask = (submask - 1) & mask
            
            return go(index + 1, mask)
        
        return go(0, (1 << m) - 1)
            
            
        
        
```


