---
id: max-consecutive-ones-iii
title: Max Consecutive Ones III
description: Problem Description and Solution for Max Consecutive Ones III
sidebar_label: 1004. Max Consecutive Ones III
sidebar_position: 1004
---

# [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

```py title=max-consecutive-ones-iii.py
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        
        for j in range(n):
            if nums[j] == 0:
                k -= 1
            
            if k < 0:
                if nums[i] == 0:
                    k += 1
                
                i += 1
        
        return j - i + 1
```


