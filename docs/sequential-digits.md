---
id: sequential-digits
title: Sequential Digits
description: Problem Description and Solution for Sequential Digits
sidebar_label: 1291. Sequential Digits
sidebar_position: 1291
---

# [1291. Sequential Digits](https://leetcode.com/problems/sequential-digits/)

```py title=sequential-digits.py
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        q = collections.deque(range(1,10))
        res = []
        
        while q:
            v = q.popleft()
            if low <= v <= high:
                res.append(v)
            
            last = v%10
            
            if last < 9:
                q.append(v*10 + last + 1)
        
        return res
```


