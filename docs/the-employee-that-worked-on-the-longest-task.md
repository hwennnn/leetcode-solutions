---
id: the-employee-that-worked-on-the-longest-task
title: The Employee That Worked on the Longest Task
description: Problem Description and Solution for The Employee That Worked on the Longest Task
sidebar_label: 2432. The Employee That Worked on the Longest Task
sidebar_position: 2432
---

# [2432. The Employee That Worked on the Longest Task](https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/)

```py title=the-employee-that-worked-on-the-longest-task.py
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        longest = -inf
        res = -1
        prev = 0
        
        for eID, d in logs:
            duration = d - prev
            
            if duration > longest:
                longest = duration
                res = eID
            elif duration == longest and eID < res:
                res = eID
                
            prev = d
        
        return res
```


