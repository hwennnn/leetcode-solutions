---
id: form-array-by-concatenating-subarrays-of-another-array
title: Form Array by Concatenating Subarrays of Another Array
description: Problem Description and Solution for Form Array by Concatenating Subarrays of Another Array
sidebar_label: 1764. Form Array by Concatenating Subarrays of Another Array
sidebar_position: 1764
---

# [1764. Form Array by Concatenating Subarrays of Another Array](https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/)

```py title=form-array-by-concatenating-subarrays-of-another-array.py
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        
        for grp in groups:
            for ii in range(i, len(nums)):
                if nums[ii: ii + len(grp)] == grp:
                    i = ii + len(grp)
                    break
            else:
                return False
        
        return True
```


