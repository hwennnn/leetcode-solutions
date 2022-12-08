---
id: x-of-a-kind-in-a-deck-of-cards
title: X of a Kind in a Deck of Cards
description: Problem Description and Solution for X of a Kind in a Deck of Cards
sidebar_label: 914. X of a Kind in a Deck of Cards
sidebar_position: 914
---

# [914. X of a Kind in a Deck of Cards](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/)

```py title=x-of-a-kind-in-a-deck-of-cards.py
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        count = collections.Counter(deck)
        
        mini = min(count.values())
        
        if mini < 2: return False
        
        for i in range(mini,1,-1):
            check = all(value % i == 0 for value in count.values())

            if check: return True
            
        return False
                
            
```


