---
id: find-minimum-in-rotated-sorted-array-ii
title: Find Minimum in Rotated Sorted Array II
description: Problem Description and Solution for Find Minimum in Rotated Sorted Array II
sidebar_label: 154. Find Minimum in Rotated Sorted Array II
sidebar_position: 154
---

# [154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

```py title=find-minimum-in-rotated-sorted-array-ii.py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        
        return nums[left]
```


