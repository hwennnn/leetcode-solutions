---
id: consecutive-characters
title: Consecutive Characters
description: Problem Description and Solution for Consecutive Characters
sidebar_label: 1446. Consecutive Characters
sidebar_position: 1446
---

# [1446. Consecutive Characters](https://leetcode.com/problems/consecutive-characters/)

```py title=consecutive-characters.py
class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        curr = s[0]
        count = res = 1
        
        for i in range(1, n):
            if s[i] == curr:
                count += 1
            else:
                count = 1
                curr = s[i]
            
            res = max(res, count)
        
        return res
```


