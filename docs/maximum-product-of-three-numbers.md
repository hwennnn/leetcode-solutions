---
id: maximum-product-of-three-numbers
title: Maximum Product of Three Numbers
description: Problem Description and Solution for Maximum Product of Three Numbers
sidebar_label: 628. Maximum Product of Three Numbers
sidebar_position: 628
---

# [628. Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/)

```py title=maximum-product-of-three-numbers.py
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2 : return 0
        
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
```


