---
id: minimum-amount-of-time-to-collect-garbage
title: Minimum Amount of Time to Collect Garbage
description: Problem Description and Solution for Minimum Amount of Time to Collect Garbage
sidebar_label: 2391. Minimum Amount of Time to Collect Garbage
sidebar_position: 2391
---

# [2391. Minimum Amount of Time to Collect Garbage](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/)

```py title=minimum-amount-of-time-to-collect-garbage.py
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        lastM = lastP = lastG = -1
        res = 0
        
        for index, gar in enumerate(garbage):
            for gType in gar:
                if gType == "M":
                    lastM = index
                    res += 1
                elif gType == "P":
                    lastP = index
                    res += 1
                else:
                    lastG = index
                    res += 1
        
        for i in range(lastM):
            res += travel[i]
            
        for i in range(lastP):
            res += travel[i]
            
        for i in range(lastG):
            res += travel[i]
            
        return res
        
```


