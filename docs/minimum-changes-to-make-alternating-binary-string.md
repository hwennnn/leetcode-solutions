---
id: minimum-changes-to-make-alternating-binary-string
title: Minimum Changes To Make Alternating Binary String
description: Problem Description and Solution for Minimum Changes To Make Alternating Binary String
sidebar_label: 1758. Minimum Changes To Make Alternating Binary String
sidebar_position: 1758
---

# [1758. Minimum Changes To Make Alternating Binary String](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/)

```py title=minimum-changes-to-make-alternating-binary-string.py
class Solution:
    def minOperations(self, s: str) -> int:
        
        n = len(s)
        
        first, second = ["1"], ["0"]
        
        for _ in range(n-1):
            first.append(second[-1])
            second.append(first[-2])
        
        def diff(word):
            return sum(a != b for a,b in zip(word, s))
        
        return min(diff(first), diff(second))
            
```


