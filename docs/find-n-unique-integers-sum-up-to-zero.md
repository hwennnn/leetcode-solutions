---
id: find-n-unique-integers-sum-up-to-zero
title: Find N Unique Integers Sum up to Zero
description: Problem Description and Solution for Find N Unique Integers Sum up to Zero
sidebar_label: 1304. Find N Unique Integers Sum up to Zero
sidebar_position: 1304
---

# [1304. Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)

```py title=find-n-unique-integers-sum-up-to-zero.py
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n & 1: res.append(0)
            
        for i in range(-1000,-1000+n//2):
            res.append(i)


        for i in range(1000, 1000 - n//2, -1):
            res.append(i)

        
        return res
            
```


