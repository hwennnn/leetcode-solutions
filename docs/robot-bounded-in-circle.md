---
id: robot-bounded-in-circle
title: Robot Bounded In Circle
description: Problem Description and Solution for Robot Bounded In Circle
sidebar_label: 1041. Robot Bounded In Circle
sidebar_position: 1041
---

# [1041. Robot Bounded In Circle](https://leetcode.com/problems/robot-bounded-in-circle/)

```py title=robot-bounded-in-circle.py
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = i = 0
        
        for c in instructions:
            if c == "R":
                i = (i + 1) % 4
            elif c == "L":
                i = (i + 3) % 4
            else:
                x, y = x + d[i][0], y + d[i][1]
        
        return (x, y) == (0, 0) or i > 0
```


