---
id: implement-queue-using-stacks
title: Implement Queue using Stacks
description: Problem Description and Solution for Implement Queue using Stacks
sidebar_label: 232. Implement Queue using Stacks
sidebar_position: 232
---

# [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

```py title=implement-queue-using-stacks.py
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
    
    def empty(self) -> bool:
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```


