---
id: next-greater-element-ii
title: Next Greater Element II
description: Problem Description and Solution for Next Greater Element II
sidebar_label: 503. Next Greater Element II
sidebar_position: 503
---

# [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)

```py title=next-greater-element-ii.py
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        nums += nums
        
        for i, x in enumerate(nums):
            while stack and x > nums[stack[-1]]:
                res[stack.pop()] = x
            
            stack.append(i % n)
        
        return res
```


