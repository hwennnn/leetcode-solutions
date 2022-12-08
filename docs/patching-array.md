---
id: patching-array
title: Patching Array
description: Problem Description and Solution for Patching Array
sidebar_label: 330. Patching Array
sidebar_position: 330
---

# [330. Patching Array](https://leetcode.com/problems/patching-array/)

```py title=patching-array.py
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss, i, res = 1, 0, 0
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                res += 1
        
        return res
```


