---
id: flip-string-to-monotone-increasing
title: Flip String to Monotone Increasing
description: Problem Description and Solution for Flip String to Monotone Increasing
sidebar_label: 926. Flip String to Monotone Increasing
sidebar_position: 926
---

# [926. Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/)

```py title=flip-string-to-monotone-increasing.py
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flipCount = onesCount = 0
        
        for c in s:
            if c == '0':
                if onesCount == 0:
                    continue
                else:
                    flipCount += 1
            else:
                onesCount += 1
            
            if flipCount > onesCount:
                flipCount = onesCount
        
        return flipCount
```


