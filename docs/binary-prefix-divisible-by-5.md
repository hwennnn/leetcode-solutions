---
id: binary-prefix-divisible-by-5
title: Binary Prefix Divisible By 5
description: Problem Description and Solution for Binary Prefix Divisible By 5
sidebar_label: 1018. Binary Prefix Divisible By 5
sidebar_position: 1018
---

# [1018. Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/)

```py title=binary-prefix-divisible-by-5.py
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        prev = 0
        res = []
        
        for x in nums:
            prev = prev * 2 + x
            res.append(prev % 5 == 0)
        
        return res
```


