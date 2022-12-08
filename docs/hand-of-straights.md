---
id: hand-of-straights
title: Hand of Straights
description: Problem Description and Solution for Hand of Straights
sidebar_label: 846. Hand of Straights
sidebar_position: 846
---

# [846. Hand of Straights](https://leetcode.com/problems/hand-of-straights/)

```py title=hand-of-straights.py
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0: return False
        
        c = collections.Counter(hand)
        sc = sorted(c.keys())
        
        def findStart():
            for key in sc:
                if c[key] > 0: return key

        for _ in range(n // W):
            start = findStart()

            for i in range(start, start+W):
                if c[i] > 0:
                    c[i] -= 1
                else:
                    return False
        
        return True
                
        
        
```


