---
id: student-attendance-record-i
title: Student Attendance Record I
description: Problem Description and Solution for Student Attendance Record I
sidebar_label: 551. Student Attendance Record I
sidebar_position: 551
---

# [551. Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/)

```py title=student-attendance-record-i.py
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count("A")<2 and s.count("LLL")==0
```


