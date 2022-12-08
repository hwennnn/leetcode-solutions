---
id: find-all-numbers-disappeared-in-an-array
title: Find All Numbers Disappeared in an Array
description: Problem Description and Solution for Find All Numbers Disappeared in an Array
sidebar_label: 448. Find All Numbers Disappeared in an Array
sidebar_position: 448
---

# [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

```py title=find-all-numbers-disappeared-in-an-array.py
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        for i, x in enumerate(nums):
            x = abs(x) - 1
            nums[x] = -abs(nums[x])
        
        for i, x in enumerate(nums):
            if x > 0:
                res.append(i + 1)
        
        return res
        
        
```


