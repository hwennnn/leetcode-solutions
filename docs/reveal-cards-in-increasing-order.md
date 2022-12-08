---
id: reveal-cards-in-increasing-order
title: Reveal Cards In Increasing Order
description: Problem Description and Solution for Reveal Cards In Increasing Order
sidebar_label: 950. Reveal Cards In Increasing Order
sidebar_position: 950
---

# [950. Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order/)

```py title=reveal-cards-in-increasing-order.py
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        res = [0] * n
        queue = deque([i for i in range(n)])
        
        deck.sort()
        
        for i in range(n):
            index = queue.popleft()
            res[index] = deck[i]
            if queue:
                queue.append(queue.popleft())
        
        return res
        
```


