---
id: queries-on-a-permutation-with-key
title: Queries on a Permutation With Key
description: Problem Description and Solution for Queries on a Permutation With Key
sidebar_label: 1409. Queries on a Permutation With Key
sidebar_position: 1409
---

# [1409. Queries on a Permutation With Key](https://leetcode.com/problems/queries-on-a-permutation-with-key/)

```py title=queries-on-a-permutation-with-key.py
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [i for i in range(1,m+1)]
        res = []
        for i,q in enumerate(queries):
            for j, num in enumerate(arr):
                if num == q:
                    res.append(j)
                    arr.pop(j)
                    arr.insert(0,num)
                    break
        
        return res
```


