---
id: find-first-and-last-position-of-element-in-sorted-array
title: Find First and Last Position of Element in Sorted Array
description: Problem Description and Solution for Find First and Last Position of Element in Sorted Array
sidebar_label: 34. Find First and Last Position of Element in Sorted Array
sidebar_position: 34
---

# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

```py title=find-first-and-last-position-of-element-in-sorted-array.py
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        res = [bisect_left(nums, target), bisect_left(nums, target + 1) - 1]
        return [-1, -1] if res[0] >= n or nums[res[0]] != target else res
```


