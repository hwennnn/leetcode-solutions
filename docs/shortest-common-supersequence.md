---
id: shortest-common-supersequence
title: Shortest Common Supersequence 
description: Problem Description and Solution for Shortest Common Supersequence 
sidebar_label: 1092. Shortest Common Supersequence 
sidebar_position: 1092
---

# [1092. Shortest Common Supersequence ](https://leetcode.com/problems/shortest-common-supersequence/)

```py title=shortest-common-supersequence.py
class Solution:
    def shortestCommonSupersequence(self, A: str, B: str) -> str:
        def lcs():
            m, n = len(A), len(B)
            dp = [[""] * (n + 1) for _ in range(m + 1)]
            
            for i in range(m):
                for j in range(n):
                    if A[i] == B[j]:
                        dp[i + 1][j + 1] = dp[i][j] + A[i]
                    else:
                        dp[i + 1][j + 1] += max(dp[i + 1][j], dp[i][j + 1], key = len)
            
            return dp[-1][-1]
        
        res, i, j = '', 0, 0
        
        for c in lcs():
            while A[i] != c:
                res += A[i]
                i += 1
            
            while B[j] != c:
                res += B[j]
                j += 1
            
            res += c
            i, j = i + 1, j + 1
        
        return res + A[i:] + B[j:]
```


