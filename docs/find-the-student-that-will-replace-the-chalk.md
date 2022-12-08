---
id: find-the-student-that-will-replace-the-chalk
title: Find the Student that Will Replace the Chalk
description: Problem Description and Solution for Find the Student that Will Replace the Chalk
sidebar_label: 1894. Find the Student that Will Replace the Chalk
sidebar_position: 1894
---

# [1894. Find the Student that Will Replace the Chalk](https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/)

```py title=find-the-student-that-will-replace-the-chalk.py
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)
        k %= total
        
        for i, x in enumerate(chalk):
            if k < x: return i
            k -= x
```


