---
id: length-of-the-longest-alphabetical-continuous-substring
title: Length of the Longest Alphabetical Continuous Substring
description: Problem Description and Solution for Length of the Longest Alphabetical Continuous Substring
sidebar_label: 2414. Length of the Longest Alphabetical Continuous Substring
sidebar_position: 2414
---

# [2414. Length of the Longest Alphabetical Continuous Substring](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/)

```py title=length-of-the-longest-alphabetical-continuous-substring.py
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        N = len(s)
        res = length = 1
        
        def f(x):
            return ord(x) - ord("a")
        
        prev = f(s[0])
        
        for i in range(1, N):
            curr = f(s[i])
            
            if prev + 1 == curr:
                length += 1
                res = max(res, length)
            else:
                length = 1
            
            prev = curr
        
        return res
```


