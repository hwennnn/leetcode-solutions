---
id: beautiful-array
title: Beautiful Array
description: Problem Description and Solution for Beautiful Array
sidebar_label: 932. Beautiful Array
sidebar_position: 932
---

# [932. Beautiful Array](https://leetcode.com/problems/beautiful-array/)

```py title=beautiful-array.py
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        return sorted(range(1, N + 1), key = lambda x : bin(x)[:1:-1])
```


