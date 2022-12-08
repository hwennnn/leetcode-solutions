---
id: maximum-number-of-groups-entering-a-competition
title: Maximum Number of Groups Entering a Competition
description: Problem Description and Solution for Maximum Number of Groups Entering a Competition
sidebar_label: 2358. Maximum Number of Groups Entering a Competition
sidebar_position: 2358
---

# [2358. Maximum Number of Groups Entering a Competition](https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/)

```py title=maximum-number-of-groups-entering-a-competition.py
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        
        def good(k):
            return (k * (k + 1)) // 2 <= n
        
        left, right = 0, n
        
        while left < right:
            mid = (left + right + 1) // 2
            
            if good(mid):
                left = mid
            else:
                right = mid - 1

        return left
```


