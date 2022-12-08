---
id: check-if-binary-string-has-at-most-one-segment-of-ones
title: Check if Binary String Has at Most One Segment of Ones
description: Problem Description and Solution for Check if Binary String Has at Most One Segment of Ones
sidebar_label: 1784. Check if Binary String Has at Most One Segment of Ones
sidebar_position: 1784
---

# [1784. Check if Binary String Has at Most One Segment of Ones](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/)

```py title=check-if-binary-string-has-at-most-one-segment-of-ones.py
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
```


