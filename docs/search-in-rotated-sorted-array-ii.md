---
id: search-in-rotated-sorted-array-ii
title: Search in Rotated Sorted Array II
description: Problem Description and Solution for Search in Rotated Sorted Array II
sidebar_label: 81. Search in Rotated Sorted Array II
sidebar_position: 81
---

# [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

```py title=search-in-rotated-sorted-array-ii.py
class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return nums[l] == target
        
```


