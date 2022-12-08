---
id: contains-duplicate-iii
title: Contains Duplicate III
description: Problem Description and Solution for Contains Duplicate III
sidebar_label: 220. Contains Duplicate III
sidebar_position: 220
---

# [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)

```py title=contains-duplicate-iii.py
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if t < 0: return False
        d = {}
        w = t + 1
        
        
        for i,n in enumerate(nums):
            m = n // w
            if m in d:
                return True
            if m - 1 in d and abs(n - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(n - d[m + 1]) < w:
                return True
            d[m] = n

            if i >= k: del d[nums[i - k] // w]
        return False

```


