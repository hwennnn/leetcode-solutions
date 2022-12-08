---
id: minimum-moves-to-reach-target-score
title: Minimum Moves to Reach Target Score
description: Problem Description and Solution for Minimum Moves to Reach Target Score
sidebar_label: 2139. Minimum Moves to Reach Target Score
sidebar_position: 2139
---

# [2139. Minimum Moves to Reach Target Score](https://leetcode.com/problems/minimum-moves-to-reach-target-score/)

```py title=minimum-moves-to-reach-target-score.py
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        
        while target > 1:
            if target % 2 == 0:
                if maxDoubles > 0:
                    target //= 2
                    maxDoubles -= 1
                    res += 1
                else:
                    return res + target - 1
            else:
                target -= 1
                res += 1
        
        return res
```


