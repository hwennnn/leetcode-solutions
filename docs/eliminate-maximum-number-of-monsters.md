---
id: eliminate-maximum-number-of-monsters
title: Eliminate Maximum Number of Monsters
description: Problem Description and Solution for Eliminate Maximum Number of Monsters
sidebar_label: 1921. Eliminate Maximum Number of Monsters
sidebar_position: 1921
---

# [1921. Eliminate Maximum Number of Monsters](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/)

```py title=eliminate-maximum-number-of-monsters.py
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        for i, (d,s) in enumerate(zip(dist, speed)):
            tt = d // s + int(d % s != 0)
            dist[i] = tt
        
        dist.sort()
        res = t = 0

        for tt in dist:
            if tt > t:
                res += 1
            else:
                break
            
            t += 1
        
        return res
```


