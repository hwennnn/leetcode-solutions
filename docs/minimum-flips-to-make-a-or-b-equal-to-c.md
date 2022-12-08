---
id: minimum-flips-to-make-a-or-b-equal-to-c
title: Minimum Flips to Make a OR b Equal to c
description: Problem Description and Solution for Minimum Flips to Make a OR b Equal to c
sidebar_label: 1318. Minimum Flips to Make a OR b Equal to c
sidebar_position: 1318
---

# [1318. Minimum Flips to Make a OR b Equal to c](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

```py title=minimum-flips-to-make-a-or-b-equal-to-c.py
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        equal = (a | b) ^ c
        res = 0
        
        for i in range(31):
            mask = 1 << i
            
            if (mask & equal) > 0:
                res += 2 if (a&mask) == (b&mask) and c & mask == 0 else 1
        
        return res
```


