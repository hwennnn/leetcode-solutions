---
id: append-k-integers-with-minimal-sum
title: Append K Integers With Minimal Sum
description: Problem Description and Solution for Append K Integers With Minimal Sum
sidebar_label: 2195. Append K Integers With Minimal Sum
sidebar_position: 2195
---

# [2195. Append K Integers With Minimal Sum](https://leetcode.com/problems/append-k-integers-with-minimal-sum/)

```py title=append-k-integers-with-minimal-sum.py
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)
        
        if nums[-1] <= k + n:
            return (k + n) * (k + n + 1) // 2 - sum(nums)
        
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] - mid > k:
                right = mid
            else:
                left = mid + 1
        
        return (left + k) * (left + k + 1) // 2 - sum(nums[:left])
```


