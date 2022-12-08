---
id: incremental-memory-leak
title: Incremental Memory Leak
description: Problem Description and Solution for Incremental Memory Leak
sidebar_label: 1860. Incremental Memory Leak
sidebar_position: 1860
---

# [1860. Incremental Memory Leak](https://leetcode.com/problems/incremental-memory-leak/)

```py title=incremental-memory-leak.py
class Solution:
    def memLeak(self, m1: int, m2: int) -> List[int]:
        t = 1
        sticks = [m1, m2]
        
        while True:
            if t > max(sticks):
                return [t, *sticks]
            
            if sticks[0] >= sticks[1]:
                sticks[0] -= t
            else:
                sticks[1] -= t
            
            t += 1
            
```


