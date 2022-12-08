---
id: xor-queries-of-a-subarray
title: XOR Queries of a Subarray
description: Problem Description and Solution for XOR Queries of a Subarray
sidebar_label: 1310. XOR Queries of a Subarray
sidebar_position: 1310
---

# [1310. XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray/)

```py title=xor-queries-of-a-subarray.py
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        prefix = [0]
        for x in arr:
            prefix.append(x ^ prefix[-1])
        
        for l,r in queries:
            res.append(prefix[l] ^ prefix[r+1])
        
        return res
```


