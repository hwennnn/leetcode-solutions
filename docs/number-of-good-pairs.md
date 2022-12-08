---
id: number-of-good-pairs
title: Number of Good Pairs
description: Problem Description and Solution for Number of Good Pairs
sidebar_label: 1512. Number of Good Pairs
sidebar_position: 1512
---

# [1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)

```py title=number-of-good-pairs.py
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    res += 1
        
        return res
```


