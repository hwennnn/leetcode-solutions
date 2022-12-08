---
id: first-day-where-you-have-been-in-all-the-rooms
title: First Day Where You Have Been in All the Rooms
description: Problem Description and Solution for First Day Where You Have Been in All the Rooms
sidebar_label: 1997. First Day Where You Have Been in All the Rooms
sidebar_position: 1997
---

# [1997. First Day Where You Have Been in All the Rooms](https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/)

```py title=first-day-where-you-have-been-in-all-the-rooms.py
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n
        
        for i in range(1, n):
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % (10 ** 9 + 7)
        
        return dp[-1]
```


