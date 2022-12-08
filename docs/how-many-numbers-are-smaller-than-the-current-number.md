---
id: how-many-numbers-are-smaller-than-the-current-number
title: How Many Numbers Are Smaller Than the Current Number
description: Problem Description and Solution for How Many Numbers Are Smaller Than the Current Number
sidebar_label: 1365. How Many Numbers Are Smaller Than the Current Number
sidebar_position: 1365
---

# [1365. How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)

```py title=how-many-numbers-are-smaller-than-the-current-number.py
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * 101
        res = [0] * n
        
        for c in nums:
            counts[c] += 1
            
        for i in range(1,101):
            counts[i] += counts[i-1]
            
        for i, num in enumerate(nums):
            if num != 0:
                res[i] = counts[num-1]
        
        return res
```


