---
id: check-if-move-is-legal
title: Check if Move is Legal
description: Problem Description and Solution for Check if Move is Legal
sidebar_label: 1958. Check if Move is Legal
sidebar_position: 1958
---

# [1958. Check if Move is Legal](https://leetcode.com/problems/check-if-move-is-legal/)

```py title=check-if-move-is-legal.py
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        d = [-1, 0, 1]
        
        for di in d:
            for dj in d:
                x, y = rMove + di, cMove + dj
                
                if 0 <= x < 8 and 0 <= y < 8 and board[x][y] != color:
                    count = 0
                    clr = color
                    while 0 <= x < 8 and 0 <= y < 8 and board[x][y] != '.':
                        if clr != board[x][y]:
                            count += 1
                            if count == 2: return True
                            clr = board[x][y]
                        x += di
                        y += dj
                
        return False
```


