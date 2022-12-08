---
id: find-the-middle-index-in-array
title: Find the Middle Index in Array
description: Problem Description and Solution for Find the Middle Index in Array
sidebar_label: 1991. Find the Middle Index in Array
sidebar_position: 1991
---

# [1991. Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array/)

```py title=find-the-middle-index-in-array.py
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        for i,x in enumerate(nums):
            left = sum(nums[:i]) if i > 0 else 0
            right = sum(nums[i + 1:]) if i < len(nums) else 0

            if left == right:
                return i
        
        return -1
```


