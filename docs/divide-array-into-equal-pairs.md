---
id: divide-array-into-equal-pairs
title: Divide Array Into Equal Pairs
description: Problem Description and Solution for Divide Array Into Equal Pairs
sidebar_label: 2206. Divide Array Into Equal Pairs
sidebar_position: 2206
---

# [2206. Divide Array Into Equal Pairs](https://leetcode.com/problems/divide-array-into-equal-pairs/)

```py title=divide-array-into-equal-pairs.py
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        N = len(nums)
        n = N // 2
        
        counter = Counter(nums)
        
        for k, v in counter.items():
            if v == 1: return False
            
            n -= v // 2
        
        return n == 0
```


