---
id: minimum-adjacent-swaps-for-k-consecutive-ones
title: Minimum Adjacent Swaps for K Consecutive Ones
description: Problem Description and Solution for Minimum Adjacent Swaps for K Consecutive Ones
sidebar_label: 1703. Minimum Adjacent Swaps for K Consecutive Ones
sidebar_position: 1703
---

# [1703. Minimum Adjacent Swaps for K Consecutive Ones](https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/)

```py title=minimum-adjacent-swaps-for-k-consecutive-ones.py
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = [i for i,x in enumerate(nums) if x]
        n = len(ones)
        
        prefix = [0]
        for p in ones:
            prefix.append(prefix[-1] + p)
            
        res = float('inf')

        for i in range(n - k + 1):
            right = prefix[i+k] - prefix[k//2 + i]
            left = prefix[(k+1)//2 + i] - prefix[i]
            res = min(res, right - left)
        
        res -= (k//2)*((k+1)//2)
        
        return res
```


