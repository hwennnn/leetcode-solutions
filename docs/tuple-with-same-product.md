---
id: tuple-with-same-product
title: Tuple with Same Product
description: Problem Description and Solution for Tuple with Same Product
sidebar_label: 1726. Tuple with Same Product
sidebar_position: 1726
---

# [1726. Tuple with Same Product](https://leetcode.com/problems/tuple-with-same-product/)

```py title=tuple-with-same-product.py
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        mp = Counter()
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                
                res += mp[product]
                
                mp[product] += 1
            
        
        return res * 8
```


