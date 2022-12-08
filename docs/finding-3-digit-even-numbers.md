---
id: finding-3-digit-even-numbers
title: Finding 3-Digit Even Numbers
description: Problem Description and Solution for Finding 3-Digit Even Numbers
sidebar_label: 2094. Finding 3-Digit Even Numbers
sidebar_position: 2094
---

# [2094. Finding 3-Digit Even Numbers](https://leetcode.com/problems/finding-3-digit-even-numbers/)

```py title=finding-3-digit-even-numbers.py
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)
        
        for i in range(n):
            if digits[i] == 0: continue
            for j in range(n):
                if i == j: continue
                for k in range(n):
                    if i == k or j == k or digits[k] & 1: continue
                    res.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        
        return sorted(list(res))
```


