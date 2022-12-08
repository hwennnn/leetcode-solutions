---
id: longest-binary-subsequence-less-than-or-equal-to-k
title: Longest Binary Subsequence Less Than or Equal to K
description: Problem Description and Solution for Longest Binary Subsequence Less Than or Equal to K
sidebar_label: 2311. Longest Binary Subsequence Less Than or Equal to K
sidebar_position: 2311
---

# [2311. Longest Binary Subsequence Less Than or Equal to K](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/)

```py title=longest-binary-subsequence-less-than-or-equal-to-k.py
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        res = s.count("0")
        val = 0
        base = 1
        
        for x in s[::-1]:
            if val + base > k: break
                
            if x == "1":
                res += 1
                val += base
        
            base *= 2
        
        return res
        
```


