---
id: minimum-deletions-to-make-string-balanced
title: Minimum Deletions to Make String Balanced
description: Problem Description and Solution for Minimum Deletions to Make String Balanced
sidebar_label: 1653. Minimum Deletions to Make String Balanced
sidebar_position: 1653
---

# [1653. Minimum Deletions to Make String Balanced](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/)

```py title=minimum-deletions-to-make-string-balanced.py
class Solution:
    def minimumDeletions(self, s: str) -> int:
        c = collections.Counter(s)
        
        a_right = c["a"]
        b_right = c["b"]
        
        a_left = b_left = 0
        res = len(s)
        
        for c in s+"b":

            res = min(res, b_left + a_right)
                
            if c == "a":
                a_left += 1
                a_right -= 1
            else:
                b_left += 1
                b_right -= 1
            
            
        
        return res
            
```


