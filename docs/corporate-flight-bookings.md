---
id: corporate-flight-bookings
title: Corporate Flight Bookings
description: Problem Description and Solution for Corporate Flight Bookings
sidebar_label: 1109. Corporate Flight Bookings
sidebar_position: 1109
---

# [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)

```py title=corporate-flight-bookings.py
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)
        
        for start,end,seats in bookings:
            res[start - 1] += seats
            res[end] -= seats
        
        for i in range(1, n):
            res[i] += res[i - 1]
        
        return res[:-1]
```


