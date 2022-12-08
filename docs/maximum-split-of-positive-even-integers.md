---
id: maximum-split-of-positive-even-integers
title: Maximum Split of Positive Even Integers
description: Problem Description and Solution for Maximum Split of Positive Even Integers
sidebar_label: 2178. Maximum Split of Positive Even Integers
sidebar_position: 2178
---

# [2178. Maximum Split of Positive Even Integers](https://leetcode.com/problems/maximum-split-of-positive-even-integers/)

```py title=maximum-split-of-positive-even-integers.py
class Solution:
    def maximumEvenSplit(self, s: int) -> List[int]:
        if s & 1: return []
        
        res = []
        x = 2
        
        while x <= s:
            res.append(x)
            s -= x
            x += 2
            
        res[-1] += s
        
        return res
```


