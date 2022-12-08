---
id: longest-ideal-subsequence
title: Longest Ideal Subsequence
description: Problem Description and Solution for Longest Ideal Subsequence
sidebar_label: 2370. Longest Ideal Subsequence
sidebar_position: 2370
---

# [2370. Longest Ideal Subsequence](https://leetcode.com/problems/longest-ideal-subsequence/)

```py title=longest-ideal-subsequence.py
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        dp = [0] * 26
        
        for x in s:
            o = ord(x) - ord("a")
            M = 0
            
            for i in range(max(0, o - k), min(o + k, 25) + 1):
                M = max(M, dp[i])
            
            dp[o] = max(dp[o], 1 + M)
            
        return max(dp)
        
```


