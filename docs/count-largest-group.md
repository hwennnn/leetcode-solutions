---
id: count-largest-group
title: Count Largest Group
description: Problem Description and Solution for Count Largest Group
sidebar_label: 1399. Count Largest Group
sidebar_position: 1399
---

# [1399. Count Largest Group](https://leetcode.com/problems/count-largest-group/)

```py title=count-largest-group.py
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = collections.defaultdict(int)
        for i in range(1, n + 1):
            t = sum(map(int, list(str(i))))
            d[t] += 1
        return sum(1 for i in d.values() if i >= max(d.values()))

```


