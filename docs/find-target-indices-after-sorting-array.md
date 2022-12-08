---
id: find-target-indices-after-sorting-array
title: Find Target Indices After Sorting Array
description: Problem Description and Solution for Find Target Indices After Sorting Array
sidebar_label: 2089. Find Target Indices After Sorting Array
sidebar_position: 2089
---

# [2089. Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array/)

```py title=find-target-indices-after-sorting-array.py
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        
        for i, x in enumerate(nums):
            if x == target:
                res.append(i)
        
        return res
```


