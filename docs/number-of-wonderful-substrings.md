---
id: number-of-wonderful-substrings
title: Number of Wonderful Substrings
description: Problem Description and Solution for Number of Wonderful Substrings
sidebar_label: 1915. Number of Wonderful Substrings
sidebar_position: 1915
---

# [1915. Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings/)

```py title=number-of-wonderful-substrings.py
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [1] + [0] * 1023
        curr = res = 0
        
        for x in word:
            curr ^= (1 << ord(x) - ord('a'))
            res += count[curr]
            
            for bit in range(10):
                delta = 1 << bit
                res += count[curr ^ delta]
            
            count[curr] += 1
        
        return res
```


