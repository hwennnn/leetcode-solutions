---
id: minimum-operations-to-reduce-x-to-zero
title: Minimum Operations to Reduce X to Zero
description: Problem Description and Solution for Minimum Operations to Reduce X to Zero
sidebar_label: 1658. Minimum Operations to Reduce X to Zero
sidebar_position: 1658
---

# [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

```py title=minimum-operations-to-reduce-x-to-zero.py
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        
        if total == x: return n
        
        res = float('-inf')
        target = total - x
        mp = {0:-1}
        curr = 0
        
        for i, x in enumerate(nums):
            curr += x
            
            if curr - target in mp:
                res = max(res, i - mp[curr - target])
            
            if curr not in mp:
                mp[curr] = i
        
        return -1 if res == float('-inf') else n - res
```


