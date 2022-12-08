---
id: maximum-average-subarray-i
title: Maximum Average Subarray I
description: Problem Description and Solution for Maximum Average Subarray I
sidebar_label: 643. Maximum Average Subarray I
sidebar_position: 643
---

# [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

```py title=maximum-average-subarray-i.py
class Solution:
    def findMaxAverage(self, A: List[int], K: int) -> float:
        
        s = 0
        m = float('-inf')
        
        for i,x in enumerate(A):
            s += x
            
            if i >= K:
                s -= A[i-K]
            
            if i >= K-1:
                m = max(m, s)
        
        return m / K 
```


