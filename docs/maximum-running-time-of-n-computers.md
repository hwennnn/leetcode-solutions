---
id: maximum-running-time-of-n-computers
title: Maximum Running Time of N Computers
description: Problem Description and Solution for Maximum Running Time of N Computers
sidebar_label: 2141. Maximum Running Time of N Computers
sidebar_position: 2141
---

# [2141. Maximum Running Time of N Computers](https://leetcode.com/problems/maximum-running-time-of-n-computers/)

```py title=maximum-running-time-of-n-computers.py
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        def good(k):
            target = n * k
            have = 0
            
            for x in batteries:
                have += min(x, k)

            return have >= target
        
        total = sum(batteries)
        
        left, right = 0, total // n
        res = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if good(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return res
```


