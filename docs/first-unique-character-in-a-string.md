---
id: first-unique-character-in-a-string
title: First Unique Character in a String
description: Problem Description and Solution for First Unique Character in a String
sidebar_label: 387. First Unique Character in a String
sidebar_position: 387
---

# [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)

```py title=first-unique-character-in-a-string.py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = collections.Counter(s)
        
        for i, x in enumerate(s):
            if mp[x] == 1:
                return i
        
        return -1
```


