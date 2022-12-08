---
id: minimum-moves-to-reach-target-with-rotations
title: Minimum Moves to Reach Target with Rotations
description: Problem Description and Solution for Minimum Moves to Reach Target with Rotations
sidebar_label: 1210. Minimum Moves to Reach Target with Rotations
sidebar_position: 1210
---

# [1210. Minimum Moves to Reach Target with Rotations](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/)

```py title=minimum-moves-to-reach-target-with-rotations.py
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        start = (0, 0, 0, 1)
        end = (n - 1, n - 2, n - 1, n - 1)
        curr_level = {start}
        moves = 0
        visited = set()
        
        while curr_level:
            next_level = set()
            for pos in curr_level:
                visited.add(pos)
                r1, c1, r2, c2 = pos
                
                # down
                if c1 + 1 < n and grid[r1][c1+1] == 0 and c2 + 1 < n and grid[r2][c2+1] == 0:
                    if (r1, c1 + 1, r2, c2 + 1) not in visited:
                        next_level.add((r1, c1 + 1, r2, c2 + 1))
                
                # right
                if r1 + 1 < n and grid[r1+1][c1] == 0 and r2 + 1 < n and grid[r2+1][c2] == 0:
                    if (r1 + 1, c1, r2 + 1, c1) not in visited:
                        next_level.add((r1 + 1, c1, r2 + 1, c2))
                
                # clockwise
                if r1 == r2 and c2 == c1 + 1 and r1 + 1 < n and grid[r1+1][c1] + grid[r1+1][c1+1] == 0 :
                    if (r1, c1, r1 + 1, c1) not in visited:
                        next_level.add((r1, c1, r1 + 1, c1))
                
                # counter-clockwise
                if c1 == c2 and r2 == r1 + 1 and c1 + 1 < n and grid[r1][c1+1] + grid[r1+1][c1+1] == 0:
                    if (r1, c1, r1, c1 + 1) not in visited:
                        next_level.add((r1, c1, r1, c1 + 1))
                        
            if end in next_level: return moves + 1
            
            curr_level = next_level
            moves += 1
            
        return -1
```


