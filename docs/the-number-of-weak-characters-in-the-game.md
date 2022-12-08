---
id: the-number-of-weak-characters-in-the-game
title: The Number of Weak Characters in the Game
description: Problem Description and Solution for The Number of Weak Characters in the Game
sidebar_label: 1996. The Number of Weak Characters in the Game
sidebar_position: 1996
---

# [1996. The Number of Weak Characters in the Game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/)

```py title=the-number-of-weak-characters-in-the-game.py
class Solution:
    def numberOfWeakCharacters(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x : (x[0], -x[1]))
        res = 0
        stack = []
        
        for a, b in A:
            while stack and a > stack[-1][0] and b > stack[-1][1]:
                res += 1
                stack.pop()
            
            stack.append((a, b))
        
        return res
```


