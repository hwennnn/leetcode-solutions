---
id: find-minimum-in-rotated-sorted-array
title: Find Minimum in Rotated Sorted Array
description: Problem Description and Solution for Find Minimum in Rotated Sorted Array
sidebar_label: 153. Find Minimum in Rotated Sorted Array
sidebar_position: 153
---

# [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

```py title=find-minimum-in-rotated-sorted-array.py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]
            
            
```


