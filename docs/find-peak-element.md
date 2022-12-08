---
id: find-peak-element
title: Find Peak Element
description: Problem Description and Solution for Find Peak Element
sidebar_label: 162. Find Peak Element
sidebar_position: 162
---

# [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)

```py title=find-peak-element.py
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            l, r = float(-inf) if mid - 1 < 0 else nums[mid - 1], float('-inf') if mid + 1 >= n else nums[mid + 1]
            
            if l < nums[mid] and nums[mid] > r:
                return mid
            elif nums[mid] < l:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
```


