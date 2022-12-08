---
id: two-sum
title: Two Sum
description: Problem Description and Solution for Two Sum
sidebar_label: 1. Two Sum
sidebar_position: 1
---

# [1. Two Sum](https://leetcode.com/problems/two-sum/)

```py title=two-sum.py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        
        for i,x in enumerate(nums):
            if target - x in mp:
                return [mp[target - x], i]
            
            mp[x] = i
```


