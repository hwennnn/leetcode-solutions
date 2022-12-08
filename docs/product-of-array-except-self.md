---
id: product-of-array-except-self
title: Product of Array Except Self
description: Problem Description and Solution for Product of Array Except Self
sidebar_label: 238. Product of Array Except Self
sidebar_position: 238
---

# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

```py title=product-of-array-except-self.py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]
        for x in nums:
            left.append(left[-1] * x)
        
        res = [0] * n
        right = 1
        
        for i in range(n - 1, -1, -1):
            res[i] = right * left[i]
            right *= nums[i]
        
        return res
```


