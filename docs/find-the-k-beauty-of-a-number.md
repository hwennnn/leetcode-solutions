---
id: find-the-k-beauty-of-a-number
title: Find the K-Beauty of a Number
description: Problem Description and Solution for Find the K-Beauty of a Number
sidebar_label: 2269. Find the K-Beauty of a Number
sidebar_position: 2269
---

# [2269. Find the K-Beauty of a Number](https://leetcode.com/problems/find-the-k-beauty-of-a-number/)

```py title=find-the-k-beauty-of-a-number.py
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        
        res = 0
        
        for i in range(n - k + 1):
            x = s[i : i + k]
            
            if int(x) != 0 and num % int(x) == 0:
                res += 1
        
        return res
```


