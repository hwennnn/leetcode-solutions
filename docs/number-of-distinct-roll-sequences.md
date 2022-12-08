---
id: number-of-distinct-roll-sequences
title: Number of Distinct Roll Sequences
description: Problem Description and Solution for Number of Distinct Roll Sequences
sidebar_label: 2318. Number of Distinct Roll Sequences
sidebar_position: 2318
---

# [2318. Number of Distinct Roll Sequences](https://leetcode.com/problems/number-of-distinct-roll-sequences/)

```py title=number-of-distinct-roll-sequences.py
class Solution:
    def distinctSequences(self, n: int) -> int:
        M = 10 ** 9 + 7
        
        @cache
        def go(index, prev1, prev2):
            if index == n: return 1
            
            res = 0
            
            for dice in range(1, 7):
                if gcd(dice, prev1) == 1 and (prev1 == -1 or (dice != prev1 and dice != prev2)):
                    res += go(index + 1, dice, prev1)
                    res %= M
            
            return res % M
        
        return go(0, -1, -1) 
```


