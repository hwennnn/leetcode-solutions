---
id: count-asterisks
title: Count Asterisks
description: Problem Description and Solution for Count Asterisks
sidebar_label: 2315. Count Asterisks
sidebar_position: 2315
---

# [2315. Count Asterisks](https://leetcode.com/problems/count-asterisks/)

```py title=count-asterisks.py
class Solution:
    def countAsterisks(self, s: str) -> int:
        A = s.split('|')
        n = len(A)
        res = 0
        
        for i in range(0, n, 2):
            res += A[i].count("*")
        
        return res
```


