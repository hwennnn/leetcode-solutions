---
id: sort-characters-by-frequency
title: Sort Characters By Frequency
description: Problem Description and Solution for Sort Characters By Frequency
sidebar_label: 451. Sort Characters By Frequency
sidebar_position: 451
---

# [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

```py title=sort-characters-by-frequency.py
class Solution:
    def frequencySort(self, s: str) -> str:
        A = Counter(s)
        res = []

        for k, v in sorted(A.items(), key = lambda x:-x[1]):
            res += [k] * v
        
        return "".join(res)
```


