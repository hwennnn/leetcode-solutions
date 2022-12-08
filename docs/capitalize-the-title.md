---
id: capitalize-the-title
title: Capitalize the Title
description: Problem Description and Solution for Capitalize the Title
sidebar_label: 2129. Capitalize the Title
sidebar_position: 2129
---

# [2129. Capitalize the Title](https://leetcode.com/problems/capitalize-the-title/)

```py title=capitalize-the-title.py
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = []
        
        for s in title.split(" "):
            if len(s) <= 2:
                res.append(s.lower())
            else:
                res.append(s.title())
        
        return " ".join(res)
```


