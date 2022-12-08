---
id: maximum-score-after-splitting-a-string
title: Maximum Score After Splitting a String
description: Problem Description and Solution for Maximum Score After Splitting a String
sidebar_label: 1422. Maximum Score After Splitting a String
sidebar_position: 1422
---

# [1422. Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/)

```py title=maximum-score-after-splitting-a-string.py
class Solution:
    def maxScore(self, S: str) -> int:
        res = 0
        for i in range(len(S)-1):
            a = S[:i+1].count("0")
            b = S[i+1:].count("1")
            res = max(res, a+b)
        
        return res
```


