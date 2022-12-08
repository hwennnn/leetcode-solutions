---
id: minimum-consecutive-cards-to-pick-up
title: Minimum Consecutive Cards to Pick Up
description: Problem Description and Solution for Minimum Consecutive Cards to Pick Up
sidebar_label: 2260. Minimum Consecutive Cards to Pick Up
sidebar_position: 2260
---

# [2260. Minimum Consecutive Cards to Pick Up](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/)

```py title=minimum-consecutive-cards-to-pick-up.py
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float('inf')
        last = {}
        
        for j, x in enumerate(cards):
            if x in last:
                res = min(res, j - last[x] + 1)
                
            last[x] = j
        
        
        return -1 if res == float('inf') else res
```


