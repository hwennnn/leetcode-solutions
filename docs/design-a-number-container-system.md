---
id: design-a-number-container-system
title: Design a Number Container System
description: Problem Description and Solution for Design a Number Container System
sidebar_label: 2349. Design a Number Container System
sidebar_position: 2349
---

# [2349. Design a Number Container System](https://leetcode.com/problems/design-a-number-container-system/)

```py title=design-a-number-container-system.py
from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.A = {}
        self.sl = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.A:
            prevNumber = self.A[index]
            self.sl[prevNumber].remove(index)
            
        self.A[index] = number
        self.sl[number].add(index)
        

    def find(self, number: int) -> int:
        s = self.sl[number]
        
        if not s: return -1
        
        return s[0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
```


