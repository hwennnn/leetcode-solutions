---
id: brick-wall
title: Brick Wall
description: Problem Description and Solution for Brick Wall
sidebar_label: 554. Brick Wall
sidebar_position: 554
---

# [554. Brick Wall](https://leetcode.com/problems/brick-wall/)

```py title=brick-wall.py
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        
        mp = collections.defaultdict(int)
        
        for bricks in wall:
            start = 0
            for i in range(len(bricks) - 1):
                start += bricks[i]
                mp[start] += 1
        
        return n - (max(mp.values()) if len(mp) > 0 else 0)
            
```


