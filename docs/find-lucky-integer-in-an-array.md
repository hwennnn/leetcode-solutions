---
id: find-lucky-integer-in-an-array
title: Find Lucky Integer in an Array
description: Problem Description and Solution for Find Lucky Integer in an Array
sidebar_label: 1394. Find Lucky Integer in an Array
sidebar_position: 1394
---

# [1394. Find Lucky Integer in an Array](https://leetcode.com/problems/find-lucky-integer-in-an-array/)

```py title=find-lucky-integer-in-an-array.py
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        C = collections.Counter(arr)
        res = -1
        for c in C:
            if c == C[c]:
                res = max(res, c)
        
        return res
```


