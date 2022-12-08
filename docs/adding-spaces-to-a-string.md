---
id: adding-spaces-to-a-string
title: Adding Spaces to a String
description: Problem Description and Solution for Adding Spaces to a String
sidebar_label: 2109. Adding Spaces to a String
sidebar_position: 2109
---

# [2109. Adding Spaces to a String](https://leetcode.com/problems/adding-spaces-to-a-string/)

```py title=adding-spaces-to-a-string.py
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces = set(spaces)
        
        for i, x in enumerate(s):
            if i in spaces:
                res.append(" ")
            
            res.append(x)
        
        return "".join(res)
```


