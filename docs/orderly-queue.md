---
id: orderly-queue
title: Orderly Queue
description: Problem Description and Solution for Orderly Queue
sidebar_label: 899. Orderly Queue
sidebar_position: 899
---

# [899. Orderly Queue](https://leetcode.com/problems/orderly-queue/)

```py title=orderly-queue.py
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return "".join(sorted(s)) if k > 1 else min(s[i:] + s[:i] for i in range(len(s)))
```


