---
id: search-insert-position
title: Search Insert Position
description: Problem Description and Solution for Search Insert Position
sidebar_label: 35. Search Insert Position
sidebar_position: 35
---

# [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

```py title=search-insert-position.py
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left
```


