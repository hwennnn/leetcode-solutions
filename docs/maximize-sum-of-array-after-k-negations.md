---
id: maximize-sum-of-array-after-k-negations
title: Maximize Sum Of Array After K Negations
description: Problem Description and Solution for Maximize Sum Of Array After K Negations
sidebar_label: 1005. Maximize Sum Of Array After K Negations
sidebar_position: 1005
---

# [1005. Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/)

```py title=maximize-sum-of-array-after-k-negations.py
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        neg = []
        pos = []
        
        for x in nums:
            if x < 0:
                neg.append(x)
            else:
                pos.append(x)
        
        pos.sort()
        
        if k >= len(neg):
            k -= len(neg)
            nums = sorted(abs(x) for x in nums)
            
            if k % 2 == 1:
                return -nums[0] + sum(nums[1:])
            else:
                return sum(nums)
        else:
            neg.sort()
            
            return sum(pos) - sum(neg[:k]) + sum(neg[k:])
```


