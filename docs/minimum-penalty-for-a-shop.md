---
id: minimum-penalty-for-a-shop
title: Minimum Penalty for a Shop
description: Problem Description and Solution for Minimum Penalty for a Shop
sidebar_label: 2483. Minimum Penalty for a Shop
sidebar_position: 2483
---

# [2483. Minimum Penalty for a Shop](https://leetcode.com/problems/minimum-penalty-for-a-shop/)

```py title=minimum-penalty-for-a-shop.py
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        t = -1
        penalty = inf
        A = [0]
        
        for x in customers:
            k = 1 if x == "Y" else 0
            A.append(k + A[-1])
        
        o = 0
        for i in range(N + 1):
            p = o + A[-1] - A[i]
            if p < penalty:
                penalty = p
                t = i
            
            if i < N and customers[i] == "N":
                o += 1
        
        return t
```


