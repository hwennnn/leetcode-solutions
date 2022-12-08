---
id: maximum-frequency-stack
title: Maximum Frequency Stack
description: Problem Description and Solution for Maximum Frequency Stack
sidebar_label: 895. Maximum Frequency Stack
sidebar_position: 895
---

# [895. Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)

```py title=maximum-frequency-stack.py
class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.pq = []
        self.index = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        heapq.heappush(self.pq, (-self.count[val], -self.index, val))
        self.index += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.pq)
        self.count[val] -= 1
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
```


