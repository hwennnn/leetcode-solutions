---
id: design-hashset
title: Design HashSet
description: Problem Description and Solution for Design HashSet
sidebar_label: 705. Design HashSet
sidebar_position: 705
---

# [705. Design HashSet](https://leetcode.com/problems/design-hashset/)

```py title=design-hashset.py
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = [False] * (10 ** 6 + 1)
        

    def add(self, key: int) -> None:
        self.mp[key] = True

    def remove(self, key: int) -> None:
        self.mp[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.mp[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```


