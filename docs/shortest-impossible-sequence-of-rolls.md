---
id: shortest-impossible-sequence-of-rolls
title: Shortest Impossible Sequence of Rolls
description: Problem Description and Solution for Shortest Impossible Sequence of Rolls
sidebar_label: 2350. Shortest Impossible Sequence of Rolls
sidebar_position: 2350
---

# [2350. Shortest Impossible Sequence of Rolls](https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/)

```py title=shortest-impossible-sequence-of-rolls.py
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        curr = 1
        
        for x in rolls:
            seen.add(x)
            
            if len(seen) == k:
                curr += 1
                seen.clear()
        
        return curr
```


