---
id: query-kth-smallest-trimmed-number
title: Query Kth Smallest Trimmed Number
description: Problem Description and Solution for Query Kth Smallest Trimmed Number
sidebar_label: 2343. Query Kth Smallest Trimmed Number
sidebar_position: 2343
---

# [2343. Query Kth Smallest Trimmed Number](https://leetcode.com/problems/query-kth-smallest-trimmed-number/)

```py title=query-kth-smallest-trimmed-number.py
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        
        for k, trim in queries:
            A = []
            
            for i, x in enumerate(nums):
                A.append((x[-trim:], i))
            
            A.sort()
            
            res.append(A[k - 1][1])
        
        return res
            
            
```


