---
id: time-needed-to-rearrange-a-binary-string
title: Time Needed to Rearrange a Binary String
description: Problem Description and Solution for Time Needed to Rearrange a Binary String
sidebar_label: 2380. Time Needed to Rearrange a Binary String
sidebar_position: 2380
---

# [2380. Time Needed to Rearrange a Binary String](https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/)

```py title=time-needed-to-rearrange-a-binary-string.py
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        res = 0
        
        while "01" in s:
            s = s.replace("01", "10")
            res += 1
        
        return res
```


