---
id: interval-list-intersections
title: Interval List Intersections
description: Problem Description and Solution for Interval List Intersections
sidebar_label: 986. Interval List Intersections
sidebar_position: 986
---

# [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

```py title=interval-list-intersections.py
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        n, m = len(firstList), len(secondList)
        res = []
        
        while i < n and j < m:
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]
            
            s, e = max(s1, s2), min(e1, e2)
            
            if s <= e:
                res.append([s, e])
            
            if e1 <= e2:
                i += 1
            else:
                j += 1
        
        return res
```


