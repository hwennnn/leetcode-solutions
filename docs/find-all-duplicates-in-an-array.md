---
id: find-all-duplicates-in-an-array
title: Find All Duplicates in an Array
description: Problem Description and Solution for Find All Duplicates in an Array
sidebar_label: 442. Find All Duplicates in an Array
sidebar_position: 442
---

# [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

```py title=find-all-duplicates-in-an-array.py
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for i, x in enumerate(nums):
            index = abs(x) - 1
            
            if nums[index] < 0: res.append(index + 1)
            
            nums[index] = -nums[index]
        
        return res
```


