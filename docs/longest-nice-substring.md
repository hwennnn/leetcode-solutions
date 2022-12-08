---
id: longest-nice-substring
title: Longest Nice Substring
description: Problem Description and Solution for Longest Nice Substring
sidebar_label: 1763. Longest Nice Substring
sidebar_position: 1763
---

# [1763. Longest Nice Substring](https://leetcode.com/problems/longest-nice-substring/)

```py title=longest-nice-substring.py
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2: return ""
        
        mp = set(list(s))

        for i,c in enumerate(s):
            if c.upper() in mp and c.lower() in mp: continue
            
            first = self.longestNiceSubstring(s[:i])
            second = self.longestNiceSubstring(s[i+1:])
            
            return max(first, second, key = len)
        
        return s
```


