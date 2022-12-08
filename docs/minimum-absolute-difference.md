---
id: minimum-absolute-difference
title: Minimum Absolute Difference
description: Problem Description and Solution for Minimum Absolute Difference
sidebar_label: 1200. Minimum Absolute Difference
sidebar_position: 1200
---

# [1200. Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/)

```py title=minimum-absolute-difference.py
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mp = collections.defaultdict(list)
        arr.sort()
        mmin = float('inf')
        n = len(arr)
        
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            mmin = min(mmin, diff)
            mp[diff].append([arr[i - 1], arr[i]])
        
        return mp[mmin]
```


