---
id: maximum-product-difference-between-two-pairs
title: Maximum Product Difference Between Two Pairs
description: Problem Description and Solution for Maximum Product Difference Between Two Pairs
sidebar_label: 1913. Maximum Product Difference Between Two Pairs
sidebar_position: 1913
---

# [1913. Maximum Product Difference Between Two Pairs](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/)

```py title=maximum-product-difference-between-two-pairs.py
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
```


