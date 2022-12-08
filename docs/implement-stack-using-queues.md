---
id: implement-stack-using-queues
title: Implement Stack using Queues
description: Problem Description and Solution for Implement Stack using Queues
sidebar_label: 225. Implement Stack using Queues
sidebar_position: 225
---

# [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

```py title=implement-stack-using-queues.py
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```


