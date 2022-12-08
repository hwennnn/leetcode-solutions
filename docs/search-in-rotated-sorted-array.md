---
id: search-in-rotated-sorted-array
title: Search in Rotated Sorted Array
description: Problem Description and Solution for Search in Rotated Sorted Array
sidebar_label: 33. Search in Rotated Sorted Array
sidebar_position: 33
---

# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

```py title=search-in-rotated-sorted-array.py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target: return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
```


