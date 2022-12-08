---
id: number-of-days-between-two-dates
title: Number of Days Between Two Dates
description: Problem Description and Solution for Number of Days Between Two Dates
sidebar_label: 1360. Number of Days Between Two Dates
sidebar_position: 1360
---

# [1360. Number of Days Between Two Dates](https://leetcode.com/problems/number-of-days-between-two-dates/)

```py title=number-of-days-between-two-dates.py
class Solution:
    
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def f(date):
            y, m, d = map(int, date.split('-'))
            if m < 3:
                m += 12
                y -= 1
            return 365 * y + y // 4 + y // 400 - y // 100 + d + (153 * m + 8) // 5
        
        return abs(f(date1) - f(date2))
```


