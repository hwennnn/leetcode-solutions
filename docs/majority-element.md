---
id: majority-element
title: Majority Element
description: Problem Description and Solution for Majority Element
sidebar_label: 169. Majority Element
sidebar_position: 169
---

# [169. Majority Element](https://leetcode.com/problems/majority-element/)

```py title=majority-element.py
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = nums[0]
        count = 1
        
        for i in range(1, n):
            if nums[i] != majority:
                count -= 1
            else:
                count += 1
            
            if count == 0:
                majority = nums[i]
                count = 1
            
        return majority
        
        
```


