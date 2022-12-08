---
id: reformat-date
title: Reformat Date
description: Problem Description and Solution for Reformat Date
sidebar_label: 1507. Reformat Date
sidebar_position: 1507
---

# [1507. Reformat Date](https://leetcode.com/problems/reformat-date/)

```py title=reformat-date.py
class Solution:
    def reformatDate(self, date: str) -> str:
        M = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12", }
        
        D = ""
        if (len(date) == 13):
            D += date[-4:] + "-" + M[date[-8:-5]] + "-" + date[:2]
        else:
            D += date[-4:] + "-" + M[date[-8:-5]] + "-0" + date[0]
        return D
```


