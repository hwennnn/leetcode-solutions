---
id: coloring-a-border
title: Coloring A Border
description: Problem Description and Solution for Coloring A Border
sidebar_label: 1034. Coloring A Border
sidebar_position: 1034
---

# [1034. Coloring A Border](https://leetcode.com/problems/coloring-a-border/)

```py title=coloring-a-border.py
class Solution:
    def colorBorder(self, grid, row, col, color):
        seen, rows, cols = set(), len(grid), len(grid[0])

        def dfs(x, y):
            if (x, y) in seen: return True
            if not (0 <= x < rows and 0 <= y < cols and grid[x][y] == grid[row][col]):
                return False
            seen.add((x, y))
            
            if dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1) < 4:
                grid[x][y] = color
            return True
        
        dfs(row, col)
        return grid
```


