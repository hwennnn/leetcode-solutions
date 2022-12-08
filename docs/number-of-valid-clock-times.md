---
id: number-of-valid-clock-times
title: Number of Valid Clock Times
description: Problem Description and Solution for Number of Valid Clock Times
sidebar_label: 2437. Number of Valid Clock Times
sidebar_position: 2437
---

# [2437. Number of Valid Clock Times](https://leetcode.com/problems/number-of-valid-clock-times/)

```py title=number-of-valid-clock-times.py
class Solution:
    def countTime(self, time: str) -> int:
        res = 0
        
        for hour in range(24):
            for minutes in range(60):
                x = f"{hour:02}:{minutes:02}"
                
                for a, b in zip(time, x):
                    if a != b and a != "?":
                        break
                else:
                    res += 1
        
        return res
```


