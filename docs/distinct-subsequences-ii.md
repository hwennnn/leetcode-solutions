---
id: distinct-subsequences-ii
title: Distinct Subsequences II
description: Problem Description and Solution for Distinct Subsequences II
sidebar_label: 940. Distinct Subsequences II
sidebar_position: 940
---

# [940. Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/)

```py title=distinct-subsequences-ii.py
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        M = 10 ** 9 + 7
        res = 0
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if s[i] != s[j]:
                    dp[i] += dp[j]
                    dp[i] %= M
            
            res += dp[i]
            res %= M
        
        return res
```


