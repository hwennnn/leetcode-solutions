---
id: count-lattice-points-inside-a-circle
title: Count Lattice Points Inside a Circle
description: Problem Description and Solution for Count Lattice Points Inside a Circle
sidebar_label: 2249. Count Lattice Points Inside a Circle
sidebar_position: 2249
---

# [2249. Count Lattice Points Inside a Circle](https://leetcode.com/problems/count-lattice-points-inside-a-circle/)

```py title=count-lattice-points-inside-a-circle.py
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        s = set()
        
        for x, y, r in circles:
            for dy in range(y - r, y + r + 1):
                for dx in range(x - r, x + r + 1):
                    dist = (dx - x) * (dx - x) + (dy - y) * (dy - y)
                    if dist <= r * r:
                        s.add((dx, dy))
        
        return len(s)
```


