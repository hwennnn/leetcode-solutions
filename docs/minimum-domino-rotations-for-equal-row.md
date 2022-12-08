---
id: minimum-domino-rotations-for-equal-row
title: Minimum Domino Rotations For Equal Row
description: Problem Description and Solution for Minimum Domino Rotations For Equal Row
sidebar_label: 1007. Minimum Domino Rotations For Equal Row
sidebar_position: 1007
---

# [1007. Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)

```py title=minimum-domino-rotations-for-equal-row.py
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        tPos = collections.defaultdict(list)
        bPos = collections.defaultdict(list)
        res = float('inf')
        
        for i, x in enumerate(tops):
            tPos[x].append(i)
        
        for i, x in enumerate(bottoms):
            bPos[x].append(i)
        
        for k, v in tPos.items():
            A = set(range(0, n))
            
            for index in v:
                if index in A:
                    A.remove(index)
            
            for index in bPos[k]:
                if index in A:
                    A.remove(index)
            
            if len(A) == 0:
                res = min(res, n - max(len(v), len(bPos[k])))
                
        
        return -1 if res == float('inf') else res
            
```


