---
id: matrix-cells-in-distance-order
title: Matrix Cells in Distance Order
description: Problem Description and Solution for Matrix Cells in Distance Order
sidebar_label: 1030. Matrix Cells in Distance Order
sidebar_position: 1030
---

# [1030. Matrix Cells in Distance Order](https://leetcode.com/problems/matrix-cells-in-distance-order/)

```py title=matrix-cells-in-distance-order.py
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res = []
        visited = set((rCenter, cCenter))
        
        queue = deque([(rCenter, cCenter)])
        
        while queue:
            x, y = queue.popleft()

            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in visited:
                    visited.add((dx, dy))
                    queue.append((dx, dy))
                    res.append((abs(dx - rCenter) + abs(dy - cCenter), [dx, dy]))

        res.sort()
        
        return [v[1] for v in res]
```


