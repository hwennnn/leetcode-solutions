---
id: design-an-ordered-stream
title: Design an Ordered Stream
description: Problem Description and Solution for Design an Ordered Stream
sidebar_label: 1656. Design an Ordered Stream
sidebar_position: 1656
---

# [1656. Design an Ordered Stream](https://leetcode.com/problems/design-an-ordered-stream/)

```py title=design-an-ordered-stream.py
class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.arr = [None] * n
        self.n = n

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1
        self.arr[id] = value
        res = []
        for i in range(self.ptr, self.n):
            if self.arr[i] != None:
                res.append(self.arr[i])
            else:
                self.ptr = i
                break
        
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
```


