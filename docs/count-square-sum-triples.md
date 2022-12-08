---
id: count-square-sum-triples
title: Count Square Sum Triples
description: Problem Description and Solution for Count Square Sum Triples
sidebar_label: 1925. Count Square Sum Triples
sidebar_position: 1925
---

# [1925. Count Square Sum Triples](https://leetcode.com/problems/count-square-sum-triples/)

```py title=count-square-sum-triples.py
class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        mp = collections.defaultdict(int)

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                mp[a * a + b * b] += 1
        
        for c in range(1, n + 1):
            res += mp[c * c]

        
        return res
```


