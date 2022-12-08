---
id: design-hashmap
title: Design HashMap
description: Problem Description and Solution for Design HashMap
sidebar_label: 706. Design HashMap
sidebar_position: 706
---

# [706. Design HashMap](https://leetcode.com/problems/design-hashmap/)

```py title=design-hashmap.py
class MyHashMap:

    def __init__(self):
        self.mp = [-1] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        self.mp[key] = value

    def get(self, key: int) -> int:
        return self.mp[key]

    def remove(self, key: int) -> None:
        self.mp[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```


