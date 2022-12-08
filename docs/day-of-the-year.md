---
id: day-of-the-year
title: Day of the Year
description: Problem Description and Solution for Day of the Year
sidebar_label: 1154. Day of the Year
sidebar_position: 1154
---

# [1154. Day of the Year](https://leetcode.com/problems/day-of-the-year/)

```py title=day-of-the-year.py
from datetime import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        f = "%Y-%m-%d"
        dt = datetime.strptime(date, f)
        res = dt.timetuple().tm_yday        
        
        return res
```


