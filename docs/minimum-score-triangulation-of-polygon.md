---
id: minimum-score-triangulation-of-polygon
title: Minimum Score Triangulation of Polygon
description: Problem Description and Solution for Minimum Score Triangulation of Polygon
sidebar_label: 1039. Minimum Score Triangulation of Polygon
sidebar_position: 1039
---

# [1039. Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/)

```py title=minimum-score-triangulation-of-polygon.py
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        
        @cache
        def go(i, j):
            if j - i + 1 <= 2: return 0
            
            res = float('inf')
            
            for mid in range(i + 1, j):
                res = min(res, values[i] * values[mid] * values[j] + go(i, mid) + go(mid, j))
            
            return res
        
        return go(0, n - 1)
```


