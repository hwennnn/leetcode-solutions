---
id: minimum-size-subarray-sum
title: Minimum Size Subarray Sum
description: Problem Description and Solution for Minimum Size Subarray Sum
sidebar_label: 209. Minimum Size Subarray Sum
sidebar_position: 209
---

# [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

```py title=minimum-size-subarray-sum.py
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        if total < target: return 0
        
        left, right = 1, n
        
        def good(k):
            s = 0
            
            for i, x in enumerate(nums):
                if i >= k:
                    s -= nums[i - k]
                s += x
                
                if s >= target: return True
            
            return False
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
```


