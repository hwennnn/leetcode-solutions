---
id: binary-search
title: Binary Search
description: Problem Description and Solution for Binary Search
sidebar_label: 704. Binary Search
sidebar_position: 704
---

# [704. Binary Search](https://leetcode.com/problems/binary-search/)

```py title=binary-search.py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left if nums[left] == target else -1
```


