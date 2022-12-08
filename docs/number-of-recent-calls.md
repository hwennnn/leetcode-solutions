---
id: number-of-recent-calls
title: Number of Recent Calls
description: Problem Description and Solution for Number of Recent Calls
sidebar_label: 933. Number of Recent Calls
sidebar_position: 933
---

# [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)

```py title=number-of-recent-calls.py
class RecentCounter:

    def __init__(self):
        self.s = []
        self.index = 0

    def ping(self, t: int) -> int:
        self.s.append(t)
        
        while self.index < len(self.s) and not (t - 3000 <= self.s[self.index] <= t):
            self.index += 1
        
        return len(self.s) - self.index
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```


