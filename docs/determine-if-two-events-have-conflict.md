---
id: determine-if-two-events-have-conflict
title: Determine if Two Events Have Conflict
description: Problem Description and Solution for Determine if Two Events Have Conflict
sidebar_label: 2446. Determine if Two Events Have Conflict
sidebar_position: 2446
---

# [2446. Determine if Two Events Have Conflict](https://leetcode.com/problems/determine-if-two-events-have-conflict/)

```py title=determine-if-two-events-have-conflict.py
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        def parse(event):
            hours, minutes = map(int, event.split(":"))
            
            return hours * 60 + minutes
        
        s1, e1 = map(parse, event1)
        s2, e2 = map(parse, event2)
        
        return s1 <= s2 <= e1 or s2 <= s1 <= e2
```


