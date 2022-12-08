---
id: minimum-difficulty-of-a-job-schedule
title: Minimum Difficulty of a Job Schedule
description: Problem Description and Solution for Minimum Difficulty of a Job Schedule
sidebar_label: 1335. Minimum Difficulty of a Job Schedule
sidebar_position: 1335
---

# [1335. Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)

```py title=minimum-difficulty-of-a-job-schedule.py
class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        N = len(jobs)
        if N < d: return -1
        
        @cache
        def go(index, day):
            if day == d: return 0 if index == N else inf

            res = inf
            curr = 0
            for j in range(index, N):
                curr = max(curr, jobs[j])
                res = min(res, curr + go(j + 1, day + 1))
            
            return res
        
        return go(0, 0)
```


