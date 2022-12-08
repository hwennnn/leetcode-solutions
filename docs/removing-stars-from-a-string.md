---
id: removing-stars-from-a-string
title: Removing Stars From a String
description: Problem Description and Solution for Removing Stars From a String
sidebar_label: 2390. Removing Stars From a String
sidebar_position: 2390
---

# [2390. Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/)

```py title=removing-stars-from-a-string.py
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for x in s:
            if x == "*":
                stack.pop()
            else:
                stack.append(x)
        
        return "".join(stack)
```


