---
id: grid-game
title: Grid Game
description: Problem Description and Solution for Grid Game
sidebar_label: 2017. Grid Game
sidebar_position: 2017
---

# [2017. Grid Game](https://leetcode.com/problems/grid-game/)

```py title=grid-game.py
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res = top = sum(grid[0])
        bottom = 0
        
        for i in range(n):
            top -= grid[0][i]
            res = min(res, max(top, bottom))
            bottom += grid[1][i]
        
        return res
```


