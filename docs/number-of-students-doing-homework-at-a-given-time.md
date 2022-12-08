---
id: number-of-students-doing-homework-at-a-given-time
title: Number of Students Doing Homework at a Given Time
description: Problem Description and Solution for Number of Students Doing Homework at a Given Time
sidebar_label: 1450. Number of Students Doing Homework at a Given Time
sidebar_position: 1450
---

# [1450. Number of Students Doing Homework at a Given Time](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/)

```py title=number-of-students-doing-homework-at-a-given-time.py
class Solution:
    def busyStudent(self, start: List[int], end: List[int], k: int) -> int:
        
        res = 0
        for i,j in zip(start, end):
            if k >= i and k <= j:
                res += 1
        
        return res
```


