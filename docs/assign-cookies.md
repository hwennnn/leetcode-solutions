---
id: assign-cookies
title: Assign Cookies
description: Problem Description and Solution for Assign Cookies
sidebar_label: 455. Assign Cookies
sidebar_position: 455
---

# [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/)

```py title=assign-cookies.py
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        
        child = cook = 0
        
        while child<len(g) and cook<len(s):
            
            child += s[cook] >= g[child]
            cook += 1
        
        return child
```


