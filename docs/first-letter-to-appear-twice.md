---
id: first-letter-to-appear-twice
title: First Letter to Appear Twice
description: Problem Description and Solution for First Letter to Appear Twice
sidebar_label: 2351. First Letter to Appear Twice
sidebar_position: 2351
---

# [2351. First Letter to Appear Twice](https://leetcode.com/problems/first-letter-to-appear-twice/)

```py title=first-letter-to-appear-twice.py
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        
        for x in s:
            if x in seen:
                return x
            
            seen.add(x)
```


