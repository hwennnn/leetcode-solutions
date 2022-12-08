---
id: longest-common-subsequence
title: Longest Common Subsequence
description: Problem Description and Solution for Longest Common Subsequence
sidebar_label: 1143. Longest Common Subsequence
sidebar_position: 1143
---

# [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

```py title=longest-common-subsequence.py
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[m][n]
```


