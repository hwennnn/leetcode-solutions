---
id: stone-game-vi
title: Stone Game VI
description: Problem Description and Solution for Stone Game VI
sidebar_label: 1686. Stone Game VI
sidebar_position: 1686
---

# [1686. Stone Game VI](https://leetcode.com/problems/stone-game-vi/)

```py title=stone-game-vi.py
class Solution:
    def stoneGameVI(self, A: List[int], B: List[int]) -> int:
        res = sorted(zip(A,B), key = sum)
        p1 = sum(a for (a,_) in res[::-2] )
        p2 = sum(b for (_,b) in res[-2::-2])
        
        return 1 if p1 > p2 else 0 if p1 == p2 else -1
```


