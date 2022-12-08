---
id: contains-duplicate-ii
title: Contains Duplicate II
description: Problem Description and Solution for Contains Duplicate II
sidebar_label: 219. Contains Duplicate II
sidebar_position: 219
---

# [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

```py title=contains-duplicate-ii.py
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        
        for j, x in enumerate(nums):
            if x in mp and j - mp[x] <= k:
                return True
            
            mp[x] = j
        
        return False
```


