---
id: check-distances-between-same-letters
title: Check Distances Between Same Letters
description: Problem Description and Solution for Check Distances Between Same Letters
sidebar_label: 2399. Check Distances Between Same Letters
sidebar_position: 2399
---

# [2399. Check Distances Between Same Letters](https://leetcode.com/problems/check-distances-between-same-letters/)

```py title=check-distances-between-same-letters.py
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dist = {}
        
        for i, x in enumerate(s):
            if x not in dist:
                dist[x] = i
            else:
                k = ord(x) - ord("a")
                
                if distance[k] != i - dist[x] - 1:
                    return False
            
        return True
```


