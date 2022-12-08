---
id: car-pooling
title: Car Pooling
description: Problem Description and Solution for Car Pooling
sidebar_label: 1094. Car Pooling
sidebar_position: 1094
---

# [1094. Car Pooling](https://leetcode.com/problems/car-pooling/)

```py title=car-pooling.py
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        
        for num, start, end in trips:
            events.append((start, 1, num))
            events.append((end, -1, num))
        
        events.sort()
        
        for _, t, x in events:
            if t == 1:
                capacity -= x
            else:
                capacity += x
            if capacity < 0: return False
        
        return True
```


