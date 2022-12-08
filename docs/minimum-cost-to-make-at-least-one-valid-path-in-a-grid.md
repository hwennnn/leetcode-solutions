---
id: minimum-cost-to-make-at-least-one-valid-path-in-a-grid
title: Minimum Cost to Make at Least One Valid Path in a Grid
description: Problem Description and Solution for Minimum Cost to Make at Least One Valid Path in a Grid
sidebar_label: 1368. Minimum Cost to Make at Least One Valid Path in a Grid
sidebar_position: 1368
---

# [1368. Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

```py title=minimum-cost-to-make-at-least-one-valid-path-in-a-grid.py
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        d = [0, 1, 0, -1, 0]
        
        def getNextSteps(x, y, k):
            if k == 1:
                i = 0
            elif k == 2:
                i = 2
            elif k == 3:
                i = 1
            elif k == 4:
                i = 3
                
            return (x + d[i], y + d[i + 1])
        
        queue = deque([(0, 0, 0)])

        while queue:
            costs, x, y = queue.popleft()

            if costs != dist[x][y]: continue
            
            if x == rows - 1 and y == cols - 1:
                return costs
            
            nx, ny = getNextSteps(x, y, grid[x][y])
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols:
                    old = dist[dx][dy]
                    new = dist[x][y] + int(not (dx == nx and dy == ny))
                    
                    if new < old:
                        dist[dx][dy] = new
                        if dx == nx and dy == ny:
                            queue.appendleft((new, dx, dy))
                        else:
                            queue.append((new, dx, dy))
        
        return dist[-1][-1]
```


