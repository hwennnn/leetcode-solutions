---
id: course-schedule-iii
title: Course Schedule III
description: Problem Description and Solution for Course Schedule III
sidebar_label: 630. Course Schedule III
sidebar_position: 630
---

# [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)

```py title=course-schedule-iii.py
class Solution:
    def scheduleCourse(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x:x[1])
        pq = []
        curr = 0
        
        for t, l in A:
            curr += t
            heappush(pq, -t)
            if curr > l:
                curr += heappop(pq)
            
        return len(pq)
```


