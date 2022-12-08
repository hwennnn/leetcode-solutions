---
id: find-the-difference
title: Find the Difference
description: Problem Description and Solution for Find the Difference
sidebar_label: 389. Find the Difference
sidebar_position: 389
---

# [389. Find the Difference](https://leetcode.com/problems/find-the-difference/)

```py title=find-the-difference.py
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return "".join(Counter(t) - Counter(s))
```


