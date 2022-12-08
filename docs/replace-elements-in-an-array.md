---
id: replace-elements-in-an-array
title: Replace Elements in an Array
description: Problem Description and Solution for Replace Elements in an Array
sidebar_label: 2295. Replace Elements in an Array
sidebar_position: 2295
---

# [2295. Replace Elements in an Array](https://leetcode.com/problems/replace-elements-in-an-array/)

```py title=replace-elements-in-an-array.py
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {x:i for i, x in enumerate(nums)}
        
        for a, b in operations:
            currIndex = mp[a]
            nums[currIndex] = b
            mp[b] = currIndex
        
        return nums
```


