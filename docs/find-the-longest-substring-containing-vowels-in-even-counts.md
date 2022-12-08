---
id: find-the-longest-substring-containing-vowels-in-even-counts
title: Find the Longest Substring Containing Vowels in Even Counts
description: Problem Description and Solution for Find the Longest Substring Containing Vowels in Even Counts
sidebar_label: 1371. Find the Longest Substring Containing Vowels in Even Counts
sidebar_position: 1371
---

# [1371. Find the Longest Substring Containing Vowels in Even Counts](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/)

```py title=find-the-longest-substring-containing-vowels-in-even-counts.py
class Solution:
    def findTheLongestSubstring(self, S: str) -> int:
        mp = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        d = {0:-1}
        res = n = 0
        for i, s in enumerate(S):
            if s in mp:
                n ^= mp[s]
            
            if n not in d:
                d[n] = i
            
            else:
                res = max(res, i - d[n])
        
        return res
                
```


