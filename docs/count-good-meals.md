---
id: count-good-meals
title: Count Good Meals
description: Problem Description and Solution for Count Good Meals
sidebar_label: 1711. Count Good Meals
sidebar_position: 1711
---

# [1711. Count Good Meals](https://leetcode.com/problems/count-good-meals/)

```py title=count-good-meals.py
class Solution:
    def countPairs(self, A: List[int]) -> int:
        M = 10 ** 9 + 7
        res = 0
        mp = Counter(A)
        
        for i in range(22):
            p = 1 << i
            for v in mp:
                target = p - v
                if v == target:
                    res += mp[v] * (mp[v]-1)
                else:
                    res += mp[v] * mp[target]
        
        res //= 2
        
        return res % M
```


