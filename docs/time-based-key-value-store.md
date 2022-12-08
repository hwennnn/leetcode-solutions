---
id: time-based-key-value-store
title: Time Based Key-Value Store
description: Problem Description and Solution for Time Based Key-Value Store
sidebar_label: 981. Time Based Key-Value Store
sidebar_position: 981
---

# [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

```py title=time-based-key-value-store.py
class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        index = bisect_right(self.mp[key], (timestamp, chr(255)))
        
        return "" if index == 0 else self.mp[key][index - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```


