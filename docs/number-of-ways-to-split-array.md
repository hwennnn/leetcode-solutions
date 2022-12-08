---
id: number-of-ways-to-split-array
title: Number of Ways to Split Array
description: Problem Description and Solution for Number of Ways to Split Array
sidebar_label: 2270. Number of Ways to Split Array
sidebar_position: 2270
---

# [2270. Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array/)

```py title=number-of-ways-to-split-array.py
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = res = 0
        total = sum(nums)
        
        for x in nums[:-1]:
            s += x
            total -= x
            
            if s >= total:
                res += 1
        
        return res
```


