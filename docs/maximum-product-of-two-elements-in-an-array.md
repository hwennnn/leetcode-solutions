---
id: maximum-product-of-two-elements-in-an-array
title: Maximum Product of Two Elements in an Array
description: Problem Description and Solution for Maximum Product of Two Elements in an Array
sidebar_label: 1464. Maximum Product of Two Elements in an Array
sidebar_position: 1464
---

# [1464. Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)

```py title=maximum-product-of-two-elements-in-an-array.py
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0
        
        for i in range(n):
            for j in range(i+1,n):
                count = max(count, (nums[i]-1)*(nums[j]-1))
        
        return count
```


