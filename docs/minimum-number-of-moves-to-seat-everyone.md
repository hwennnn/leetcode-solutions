---
id: minimum-number-of-moves-to-seat-everyone
title: Minimum Number of Moves to Seat Everyone
description: Problem Description and Solution for Minimum Number of Moves to Seat Everyone
sidebar_label: 2037. Minimum Number of Moves to Seat Everyone
sidebar_position: 2037
---

# [2037. Minimum Number of Moves to Seat Everyone](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/)

```py title=minimum-number-of-moves-to-seat-everyone.py
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(s1 - s2) for s1, s2 in zip(sorted(seats), sorted(students)))
```


