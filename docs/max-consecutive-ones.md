---
id: max-consecutive-ones
title: Max Consecutive Ones
description: Problem Description and Solution for Max Consecutive Ones
sidebar_label: 485. Max Consecutive Ones
sidebar_position: 485
---

# [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)

```py title=max-consecutive-ones.py
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = ones = 0
        
        for x in nums:
            if x == 0:
                ones = 0
            else:
                ones += 1
        
            res = max(res, ones)
        
        return res
```


