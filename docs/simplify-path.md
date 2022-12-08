---
id: simplify-path
title: Simplify Path
description: Problem Description and Solution for Simplify Path
sidebar_label: 71. Simplify Path
sidebar_position: 71
---

# [71. Simplify Path](https://leetcode.com/problems/simplify-path/)

```py title=simplify-path.py
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []
        
        for x in s:
            if x == "..":
                if stack:
                    stack.pop()
            elif x != "" and x != ".":
                stack.append(x)

        return "/" + "/".join(stack)
```


