---
id: minimum-operations-to-make-the-array-k-increasing
title: Minimum Operations to Make the Array K-Increasing
description: Problem Description and Solution for Minimum Operations to Make the Array K-Increasing
sidebar_label: 2111. Minimum Operations to Make the Array K-Increasing
sidebar_position: 2111
---

# [2111. Minimum Operations to Make the Array K-Increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/)

```py title=minimum-operations-to-make-the-array-k-increasing.py
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        A = collections.defaultdict(list)
        
        for i, x in enumerate(arr):
            A[i % k].append(x)
        
        res = 0
        for _, s in A.items():
            lis = []
            
            for x in s:
                index = bisect.bisect(lis, x)
                
                if index < len(lis):
                    lis[index] = x
                else:
                    lis.append(x)
            
            res += len(s) - len(lis)
        
        return res
```


