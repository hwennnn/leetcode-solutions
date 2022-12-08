---
id: number-of-ways-to-select-buildings
title: Number of Ways to Select Buildings
description: Problem Description and Solution for Number of Ways to Select Buildings
sidebar_label: 2222. Number of Ways to Select Buildings
sidebar_position: 2222
---

# [2222. Number of Ways to Select Buildings](https://leetcode.com/problems/number-of-ways-to-select-buildings/)

```py title=number-of-ways-to-select-buildings.py
class Solution:
    def numberOfWays(self, s: str) -> int:
        rZero, rOne = s.count("0"), s.count("1")
        
        lZero = lOne = 0
        res = 0
        
        for x in s:
            if x == "1":
                lOne += 1
                res += lZero * rZero
                rOne -= 1
            else:
                lZero += 1
                res += lOne * rOne
                rZero -= 1

        return res
```


