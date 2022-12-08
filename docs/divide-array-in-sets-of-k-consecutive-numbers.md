---
id: divide-array-in-sets-of-k-consecutive-numbers
title: Divide Array in Sets of K Consecutive Numbers
description: Problem Description and Solution for Divide Array in Sets of K Consecutive Numbers
sidebar_label: 1296. Divide Array in Sets of K Consecutive Numbers
sidebar_position: 1296
---

# [1296. Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/)

```py title=divide-array-in-sets-of-k-consecutive-numbers.py
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0: return False
        
        count = collections.Counter(nums)
        keys = sorted(count)
        
        for key in keys:
            if count[key] > 0:
                c = count[key]
                for i in range(key, key+k):
                    if count[i] < c: return False
                    
                    count[i] -= c
            
        return True
```


