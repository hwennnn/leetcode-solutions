---
id: out-of-boundary-paths
title: Out of Boundary Paths
description: Problem Description and Solution for Out of Boundary Paths
sidebar_label: 576. Out of Boundary Paths
sidebar_position: 576
---

# [576. Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/)

```py title=out-of-boundary-paths.py
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 10 ** 9 + 7
        
        @cache
        def go(x, y, moves):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            
            if moves == maxMove: return 0
            
            res = 0
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                res += go(dx, dy, moves + 1)    
                res %= M
            
            return res
        
        return go(startRow, startColumn, 0)
```


