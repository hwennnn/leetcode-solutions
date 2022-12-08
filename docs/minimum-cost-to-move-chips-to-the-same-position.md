---
id: minimum-cost-to-move-chips-to-the-same-position
title: Minimum Cost to Move Chips to The Same Position
description: Problem Description and Solution for Minimum Cost to Move Chips to The Same Position
sidebar_label: 1217. Minimum Cost to Move Chips to The Same Position
sidebar_position: 1217
---

# [1217. Minimum Cost to Move Chips to The Same Position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/)

```py title=minimum-cost-to-move-chips-to-the-same-position.py
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0
        
        for x in position:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1
        
        return min(even, odd)
```


