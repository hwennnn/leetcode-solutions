---
id: finding-the-users-active-minutes
title: Finding the Users Active Minutes
description: Problem Description and Solution for Finding the Users Active Minutes
sidebar_label: 1817. Finding the Users Active Minutes
sidebar_position: 1817
---

# [1817. Finding the Users Active Minutes](https://leetcode.com/problems/finding-the-users-active-minutes/)

```py title=finding-the-users-active-minutes.py
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        mp = collections.defaultdict(set)
        
        for i, time in logs:
            mp[i].add(time)
        
        for v in mp.values():
            res[len(v) - 1] += 1
        
        return res
```


