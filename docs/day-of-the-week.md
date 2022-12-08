---
id: day-of-the-week
title: Day of the Week
description: Problem Description and Solution for Day of the Week
sidebar_label: 1185. Day of the Week
sidebar_position: 1185
---

# [1185. Day of the Week](https://leetcode.com/problems/day-of-the-week/)

```py title=day-of-the-week.py
class Solution:
    def dayOfTheWeek(self, d, m, y):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        from datetime import datetime
        return days[datetime(y, m, d).weekday()]
        
```


