---
id: set-mismatch
title: Set Mismatch
description: Problem Description and Solution for Set Mismatch
sidebar_label: 645. Set Mismatch
sidebar_position: 645
---

# [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/)

```py title=set-mismatch.py
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        s = set()
        dup = -1
        total = N * (N + 1) // 2
        
        for x in nums:
            if x in s:
                dup = x
            else:
                s.add(x)
                total -= x
        
        return [dup, total]
        
```


