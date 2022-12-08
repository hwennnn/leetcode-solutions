---
id: baseball-game
title: Baseball Game
description: Problem Description and Solution for Baseball Game
sidebar_label: 682. Baseball Game
sidebar_position: 682
---

# [682. Baseball Game](https://leetcode.com/problems/baseball-game/)

```py title=baseball-game.py
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for x in ops:
            if x == "C":
                stack.pop()
            elif x == "D":
                stack.append(stack[-1] * 2)
            elif x == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(x))
        
        return sum(stack)
```


