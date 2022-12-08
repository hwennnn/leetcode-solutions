---
id: rings-and-rods
title: Rings and Rods
description: Problem Description and Solution for Rings and Rods
sidebar_label: 2103. Rings and Rods
sidebar_position: 2103
---

# [2103. Rings and Rods](https://leetcode.com/problems/rings-and-rods/)

```py title=rings-and-rods.py
class Solution:
    def countPoints(self, rings: str) -> int:
        mp = collections.defaultdict(set)
        n = len(rings)
        
        for i in range(0, n, 2):
            mp[rings[i + 1]].add(rings[i])
        
        res = 0
        
        for k, v in mp.items():
            if len(v) == 3:
                res += 1

        return res
        
```


