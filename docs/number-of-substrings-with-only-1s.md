---
id: number-of-substrings-with-only-1s
title: Number of Substrings With Only 1s
description: Problem Description and Solution for Number of Substrings With Only 1s
sidebar_label: 1513. Number of Substrings With Only 1s
sidebar_position: 1513
---

# [1513. Number of Substrings With Only 1s](https://leetcode.com/problems/number-of-substrings-with-only-1s/)

```py title=number-of-substrings-with-only-1s.py
class Solution:
    def numSub(self, S: str) -> int:
        
        M = int(1e9+7)
        count = res = 0
        for s in S:
            count = count + 1 if s == "1" else 0
            res += count
        
        return res%M
```


