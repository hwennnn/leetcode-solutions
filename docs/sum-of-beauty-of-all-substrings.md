---
id: sum-of-beauty-of-all-substrings
title: Sum of Beauty of All Substrings
description: Problem Description and Solution for Sum of Beauty of All Substrings
sidebar_label: 1781. Sum of Beauty of All Substrings
sidebar_position: 1781
---

# [1781. Sum of Beauty of All Substrings](https://leetcode.com/problems/sum-of-beauty-of-all-substrings/)

```py title=sum-of-beauty-of-all-substrings.py
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0
        
        for i in range(n):
            mp = collections.defaultdict(int)
            for j in range(i, n):
                mp[s[j]] += 1
                v = mp.values()
                res += max(v) - min(v)
        
        return res
```


