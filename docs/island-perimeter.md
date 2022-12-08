---
id: island-perimeter
title: Island Perimeter
description: Problem Description and Solution for Island Perimeter
sidebar_label: 463. Island Perimeter
sidebar_position: 463
---

# [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/)

```py title=island-perimeter.py
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def go(x, y):
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] == 0: return 1
            
            visited.add((x, y))
            count = 0
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (dx, dy) not in visited:
                    count += go(dx, dy)

            return count
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    return go(x, y)
```


