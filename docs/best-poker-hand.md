---
id: best-poker-hand
title: Best Poker Hand
description: Problem Description and Solution for Best Poker Hand
sidebar_label: 2347. Best Poker Hand
sidebar_position: 2347
---

# [2347. Best Poker Hand](https://leetcode.com/problems/best-poker-hand/)

```py title=best-poker-hand.py
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1: return "Flush"
        
        if max(Counter(ranks).values()) >= 3: return "Three of a Kind"
        
        if max(Counter(ranks).values()) >= 2: return "Pair"
        
        return "High Card"
```


