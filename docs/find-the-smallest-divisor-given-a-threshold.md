---
id: find-the-smallest-divisor-given-a-threshold
title: Find the Smallest Divisor Given a Threshold
description: Problem Description and Solution for Find the Smallest Divisor Given a Threshold
sidebar_label: 1283. Find the Smallest Divisor Given a Threshold
sidebar_position: 1283
---

# [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

```py title=find-the-smallest-divisor-given-a-threshold.py
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        
        left, right = 1, max(nums)
        
        def good(k):
            count = 0
            
            for x in nums:
                count += ceil(x / k)
            
            return count <= threshold
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
```


