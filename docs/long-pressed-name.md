---
id: long-pressed-name
title: Long Pressed Name
description: Problem Description and Solution for Long Pressed Name
sidebar_label: 925. Long Pressed Name
sidebar_position: 925
---

# [925. Long Pressed Name](https://leetcode.com/problems/long-pressed-name/)

```py title=long-pressed-name.py
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)
            
        
```


