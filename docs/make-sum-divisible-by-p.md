---
id: make-sum-divisible-by-p
title: Make Sum Divisible by P
description: Problem Description and Solution for Make Sum Divisible by P
sidebar_label: 1590. Make Sum Divisible by P
sidebar_position: 1590
---

# [1590. Make Sum Divisible by P](https://leetcode.com/problems/make-sum-divisible-by-p/)

```py title=make-sum-divisible-by-p.py
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        
        mp = {0:-1}
        res = n = len(nums)
        c = 0
        
        for i,x in enumerate(nums):
            c = (c+x)%p
            mp[c] = i
            
            if (c - need)%p in mp:
                res = min(res, i - mp[(c - need) % p])
        
        return res if res != n else -1
```


