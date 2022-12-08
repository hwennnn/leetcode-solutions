---
id: subarray-with-elements-greater-than-varying-threshold
title: Subarray With Elements Greater Than Varying Threshold
description: Problem Description and Solution for Subarray With Elements Greater Than Varying Threshold
sidebar_label: 2334. Subarray With Elements Greater Than Varying Threshold
sidebar_position: 2334
---

# [2334. Subarray With Elements Greater Than Varying Threshold](https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/)

```py title=subarray-with-elements-greater-than-varying-threshold.py
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        prevSmaller = [-1] * n
        nextSmaller = [n] * n
        
        stack = []
        for i, x in enumerate(nums):
            while stack and x < nums[stack[-1]]:
                nextSmaller[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1,- 1):
            while stack and nums[i] < nums[stack[-1]]:
                prevSmaller[stack.pop()] = i
            stack.append(i)
        
        for i, x in enumerate(nums):
            left, right = prevSmaller[i], nextSmaller[i]
            
            N = right - left - 1
            
            if x > threshold // N:
                return N
        
        return -1
```


