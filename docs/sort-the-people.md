---
id: sort-the-people
title: Sort the People
description: Problem Description and Solution for Sort the People
sidebar_label: 2418. Sort the People
sidebar_position: 2418
---

# [2418. Sort the People](https://leetcode.com/problems/sort-the-people/)

```py title=sort-the-people.py
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        A = sorted([(a, b) for a, b in zip(names, heights)], key = lambda x : (-x[1]))
        
        return [a for a, _ in A]
```


