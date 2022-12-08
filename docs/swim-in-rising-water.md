---
id: swim-in-rising-water
title: Swim in Rising Water
description: Problem Description and Solution for Swim in Rising Water
sidebar_label: 778. Swim in Rising Water
sidebar_position: 778
---

# [778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

```py title=swim-in-rising-water.py
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        def dfs(x, y, mmax, visited):
            if x == y == N - 1: return True
            
            visited.add((x, y))

            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < N and 0 <= dy < N and (dx, dy) not in visited and grid[dx][dy] <= mmax:
                    if dfs(dx, dy, mmax, visited): return True
                        
            return False
            
        
        left, right = max(grid[0][0], grid[-1][-1]), 2500
        while left < right:
            mid = left + (right - left) // 2

            if dfs(0, 0, mid, set()):
                right = mid
            else:
                left = mid + 1
            
        return left
```


