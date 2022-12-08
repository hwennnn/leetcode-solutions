---
id: intersection-of-multiple-arrays
title: Intersection of Multiple Arrays
description: Problem Description and Solution for Intersection of Multiple Arrays
sidebar_label: 2248. Intersection of Multiple Arrays
sidebar_position: 2248
---

# [2248. Intersection of Multiple Arrays](https://leetcode.com/problems/intersection-of-multiple-arrays/)

```py title=intersection-of-multiple-arrays.py
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        count = Counter()
        
        for arr in nums:
            for x in arr:
                count[x] += 1
        
        res = []
        
        for k, v in count.items():
            if v == n:
                res.append(k)
        
        return sorted(res)
```


