---
id: find-the-duplicate-number
title: Find the Duplicate Number
description: Problem Description and Solution for Find the Duplicate Number
sidebar_label: 287. Find the Duplicate Number
sidebar_position: 287
---

# [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

```py title=find-the-duplicate-number.py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 1, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            count = 0
            
            for x in nums:
                if x <= mid:
                    count += 1
            
            if count <= mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
```


