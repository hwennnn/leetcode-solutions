---
id: longest-substring-with-at-least-k-repeating-characters
title: Longest Substring with At Least K Repeating Characters
description: Problem Description and Solution for Longest Substring with At Least K Repeating Characters
sidebar_label: 395. Longest Substring with At Least K Repeating Characters
sidebar_position: 395
---

# [395. Longest Substring with At Least K Repeating Characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)

```py title=longest-substring-with-at-least-k-repeating-characters.py
class Solution:
    def longestSubstring(self, st: str, k: int) -> int:
        
        res = 0
        stack = [st]
        
        while stack:
            s = stack.pop()
            for c in set(s):
                if s.count(c) < k:
                    stack.extend([ch for ch in s.split(c)])
                    break
            else:    
                res = max(res, len(s))
        
        return res
        
```


