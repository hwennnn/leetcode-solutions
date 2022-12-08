---
id: single-element-in-a-sorted-array
title: Single Element in a Sorted Array
description: Problem Description and Solution for Single Element in a Sorted Array
sidebar_label: 540. Single Element in a Sorted Array
sidebar_position: 540
---

# [540. Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)

```py title=single-element-in-a-sorted-array.py
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
```


