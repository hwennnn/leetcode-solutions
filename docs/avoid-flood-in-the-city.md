---
id: avoid-flood-in-the-city
title: Avoid Flood in The City
description: Problem Description and Solution for Avoid Flood in The City
sidebar_label: 1488. Avoid Flood in The City
sidebar_position: 1488
---

# [1488. Avoid Flood in The City](https://leetcode.com/problems/avoid-flood-in-the-city/)

```py title=avoid-flood-in-the-city.py
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = []
        dry = []
        full = {}
        
        for i, x in enumerate(rains):
            if x == 0:
                dry.append(i)
                res.append(1)
            else:
                if x in full:
                    if not dry: return []
                    
                    index = bisect_right(dry, full[x])
                    if index == len(dry): return []
                    
                    res[dry[index]] = x
                    dry.pop(index)
                    full[x] = i
                    res.append(-1)
                else:
                    full[x] = i
                    res.append(-1)
        
        return res
```


