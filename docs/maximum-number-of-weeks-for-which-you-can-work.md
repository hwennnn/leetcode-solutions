---
id: maximum-number-of-weeks-for-which-you-can-work
title: Maximum Number of Weeks for Which You Can Work
description: Problem Description and Solution for Maximum Number of Weeks for Which You Can Work
sidebar_label: 1953. Maximum Number of Weeks for Which You Can Work
sidebar_position: 1953
---

# [1953. Maximum Number of Weeks for Which You Can Work](https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/)

```py title=maximum-number-of-weeks-for-which-you-can-work.py
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        ssum, mmax = sum(milestones), max(milestones)
        
        if ssum - mmax >= mmax: return ssum
        
        return 2 * (ssum - mmax) + 1
```


