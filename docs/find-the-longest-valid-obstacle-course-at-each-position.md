---
id: find-the-longest-valid-obstacle-course-at-each-position
title: Find the Longest Valid Obstacle Course at Each Position
description: Problem Description and Solution for Find the Longest Valid Obstacle Course at Each Position
sidebar_label: 1964. Find the Longest Valid Obstacle Course at Each Position
sidebar_position: 1964
---

# [1964. Find the Longest Valid Obstacle Course at Each Position](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/)

```py title=find-the-longest-valid-obstacle-course-at-each-position.py
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        res = []
        
        for obs in obstacles:
            if len(lis) == 0 or lis[-1] <= obs:
                lis.append(obs)
                res.append(len(lis))
            else:
                index = bisect.bisect(lis, obs)
                lis[index] = obs
                res.append(index + 1)
            
        return res
```


