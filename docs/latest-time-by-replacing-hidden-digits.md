---
id: latest-time-by-replacing-hidden-digits
title: Latest Time by Replacing Hidden Digits
description: Problem Description and Solution for Latest Time by Replacing Hidden Digits
sidebar_label: 1736. Latest Time by Replacing Hidden Digits
sidebar_position: 1736
---

# [1736. Latest Time by Replacing Hidden Digits](https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/)

```py title=latest-time-by-replacing-hidden-digits.py
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        
        if time[0] == "?":
            if time[1] == "?" or int(time[1]) <= 3:
                time[0] = "2"
            else:
                time[0] = "1"
        
        if time[1] == "?":
            if time[0] == "2":
                time[1] = "3"
            elif time[0] == "1":
                time[1] = "9"
            else:
                time[1] = "9"
        
        if time[3] == "?":
            time[3] = "5"
        
        if time[4] == "?":
            time[4] = "9"
        
        return "".join(time)
            
```


