---
id: number-of-excellent-pairs
title: Number of Excellent Pairs
description: Problem Description and Solution for Number of Excellent Pairs
sidebar_label: 2354. Number of Excellent Pairs
sidebar_position: 2354
---

# [2354. Number of Excellent Pairs](https://leetcode.com/problems/number-of-excellent-pairs/)

```py title=number-of-excellent-pairs.py
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        
        MAX = 32
        bits = [0] * MAX
        
        for x in nums:
            bits[x.bit_count()] += 1
        
        res = 0
        for i in range(1, MAX):
            for j in range(1, MAX):
                if i + j >= k:
                    res += bits[i] * bits[j]
        
        return res
        
```


