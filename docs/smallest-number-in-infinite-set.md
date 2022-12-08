---
id: smallest-number-in-infinite-set
title: Smallest Number in Infinite Set
description: Problem Description and Solution for Smallest Number in Infinite Set
sidebar_label: 2336. Smallest Number in Infinite Set
sidebar_position: 2336
---

# [2336. Smallest Number in Infinite Set](https://leetcode.com/problems/smallest-number-in-infinite-set/)

```py title=smallest-number-in-infinite-set.py
class SmallestInfiniteSet:

    def __init__(self):
        self.A = [True] * (1001)
        self.index = 1

    def popSmallest(self) -> int:
        res = 0
        
        for i in range(1, len(self.A)):
            if self.A[i]:
                res = i
                self.A[i] = False
                break
        
        return res

    def addBack(self, num: int) -> None:
        self.A[num] = True


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
```


