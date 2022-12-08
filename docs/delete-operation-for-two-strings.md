---
id: delete-operation-for-two-strings
title: Delete Operation for Two Strings
description: Problem Description and Solution for Delete Operation for Two Strings
sidebar_label: 583. Delete Operation for Two Strings
sidebar_position: 583
---

# [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)

```py title=delete-operation-for-two-strings.py
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        return m + n - 2 * dp[-1][-1]
        
```


