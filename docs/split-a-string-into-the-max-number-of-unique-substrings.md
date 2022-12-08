---
id: split-a-string-into-the-max-number-of-unique-substrings
title: Split a String Into the Max Number of Unique Substrings
description: Problem Description and Solution for Split a String Into the Max Number of Unique Substrings
sidebar_label: 1593. Split a String Into the Max Number of Unique Substrings
sidebar_position: 1593
---

# [1593. Split a String Into the Max Number of Unique Substrings](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/)

```py title=split-a-string-into-the-max-number-of-unique-substrings.py
class Solution:
    def maxUniqueSplit(self, S: str) -> int:
        def backtrack(S, seen):
            res = 0
            for i in range(1, len(S)+1):
                c = S[:i]
                if c not in seen:
                    seen.add(c)
                    res = max(res, 1 + backtrack(S[i:], seen))
                    seen.remove(c)
            
            return res
        
        seen = set()
        return backtrack(S, seen)
                
        
```


