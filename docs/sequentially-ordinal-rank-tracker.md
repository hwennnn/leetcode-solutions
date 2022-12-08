---
id: sequentially-ordinal-rank-tracker
title: Sequentially Ordinal Rank Tracker
description: Problem Description and Solution for Sequentially Ordinal Rank Tracker
sidebar_label: 2102. Sequentially Ordinal Rank Tracker
sidebar_position: 2102
---

# [2102. Sequentially Ordinal Rank Tracker](https://leetcode.com/problems/sequentially-ordinal-rank-tracker/)

```py title=sequentially-ordinal-rank-tracker.py
class SORTracker:

    def __init__(self):
        self.heap = []
        self.turns = 0

    def add(self, name: str, score: int) -> None:
        bisect.insort(self.heap, (-score, name))

    def get(self) -> str:
        _, name = self.heap[self.turns]
        self.turns += 1
        
        return name


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
```


