---
id: random-pick-with-weight
title: Random Pick with Weight
description: Problem Description and Solution for Random Pick with Weight
sidebar_label: 528. Random Pick with Weight
sidebar_position: 528
---

# [528. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)

```py title=random-pick-with-weight.py
class Solution:

    def __init__(self, w: List[int]):
        self.A = list(accumulate(w))
        self.n = self.A[-1]

    def pickIndex(self) -> int:
        x = random.randint(0, self.n - 1)
        
        return bisect_right(self.A, x)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```


