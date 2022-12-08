---
id: unique-number-of-occurrences
title: Unique Number of Occurrences
description: Problem Description and Solution for Unique Number of Occurrences
sidebar_label: 1207. Unique Number of Occurrences
sidebar_position: 1207
---

# [1207. Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/)

```py title=unique-number-of-occurrences.py
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values())) == len(set(arr))
```


