---
id: uncrossed-lines
title: Uncrossed Lines
description: Problem Description and Solution for Uncrossed Lines
sidebar_label: 1035. Uncrossed Lines
sidebar_position: 1035
---

# [1035. Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/)

```py title=uncrossed-lines.py
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
            
        return dp[m][n]
```


