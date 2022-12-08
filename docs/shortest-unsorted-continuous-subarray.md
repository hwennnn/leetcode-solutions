---
id: shortest-unsorted-continuous-subarray
title: Shortest Unsorted Continuous Subarray
description: Problem Description and Solution for Shortest Unsorted Continuous Subarray
sidebar_label: 581. Shortest Unsorted Continuous Subarray
sidebar_position: 581
---

# [581. Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)

```py title=shortest-unsorted-continuous-subarray.py
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        right, prefixMax = -1, nums[0]
        
        for i in range(1, n):
            if nums[i] < prefixMax:
                right = i
            else:
                prefixMax = nums[i]
        
        if right == -1: return 0
        
        left, suffixSmall = n - 1, nums[-1]
        
        for i in range(n - 2, -1, -1):
            if nums[i] > suffixSmall:
                left = i
            else:
                suffixSmall = nums[i]
        
        return right - left + 1
```


