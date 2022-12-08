---
id: maximum-total-beauty-of-the-gardens
title: Maximum Total Beauty of the Gardens
description: Problem Description and Solution for Maximum Total Beauty of the Gardens
sidebar_label: 2234. Maximum Total Beauty of the Gardens
sidebar_position: 2234
---

# [2234. Maximum Total Beauty of the Gardens](https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/)

```py title=maximum-total-beauty-of-the-gardens.py
class Solution:
    def maximumBeauty(self, flowers: List[int], k: int, t: int, full: int, partial: int) -> int:
        n = len(flowers)
        A = [min(t, x) for x in flowers]
        A.sort()
        
        if A[0] == t: return full * n
        if k >= t * n - sum(A):
            return max(full * n, full * (n - 1) + partial * (t - 1))
        
        costs = [0]
        
        for i in range(1, n):
            costs.append(costs[-1] + (i) * (A[i] - A[i - 1]))
        
        j = n - 1
        while A[j] == t:
            j -= 1
        
        res = 0
        
        while k >= 0:
            index = min(j, bisect_right(costs, k) - 1) 
            
            minIncomplete = A[index] + (k - costs[index]) // (index + 1)
            
            res = max(res, minIncomplete * partial + full * (n - j - 1))
            
            k -= (t - A[j])
            j -= 1
            
        return res
```


