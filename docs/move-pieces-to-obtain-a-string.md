---
id: move-pieces-to-obtain-a-string
title: Move Pieces to Obtain a String
description: Problem Description and Solution for Move Pieces to Obtain a String
sidebar_label: 2337. Move Pieces to Obtain a String
sidebar_position: 2337
---

# [2337. Move Pieces to Obtain a String](https://leetcode.com/problems/move-pieces-to-obtain-a-string/)

```py title=move-pieces-to-obtain-a-string.py
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target: return True
        
        s = [(i, x) for i, x in enumerate(start) if x != "_"]
        t = [(i, x) for i, x in enumerate(target) if x != "_"]
        
        if len(t) != len(s): return False
        
        for index, (a, b) in enumerate(zip(s, t)):
            i, x = a
            j, y = b
            
            if x != y: return False

            if x == "L":
                if i < j: return False
            else:
                if i > j: return False

        
        return True
```


