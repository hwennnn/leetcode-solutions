---
id: minimum-operations-to-make-the-array-alternating
title: Minimum Operations to Make the Array Alternating
description: Problem Description and Solution for Minimum Operations to Make the Array Alternating
sidebar_label: 2170. Minimum Operations to Make the Array Alternating
sidebar_position: 2170
---

# [2170. Minimum Operations to Make the Array Alternating](https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/)

```py title=minimum-operations-to-make-the-array-alternating.py
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        odd, even = Counter(), Counter()
        
        for i, x in enumerate(nums):
            if i % 2 == 0:
                even[x] += 1
            else:
                odd[x] += 1
        
        o = sorted(odd.items(), key = lambda x : -x[1])
        e = sorted(even.items(), key = lambda x : -x[1])
        
        if o[0][0] == e[0][0]:
            res = max(o[0][1], e[0][1])
        
            if len(e) > 1:
                res = max(res, o[0][1] + e[1][1])
            
            if len(o) > 1:
                res = max(res, o[1][1] + e[0][1])
            
            return n - res
        else:
            return n - o[0][1] - e[0][1]
        
```


