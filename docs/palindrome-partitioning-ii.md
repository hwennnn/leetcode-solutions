---
id: palindrome-partitioning-ii
title: Palindrome Partitioning II
description: Problem Description and Solution for Palindrome Partitioning II
sidebar_label: 132. Palindrome Partitioning II
sidebar_position: 132
---

# [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)

```py title=palindrome-partitioning-ii.py
class Solution:
    def minCut(self, s: str) -> int:
        if len(s) == 1: return 0
        
        n = len(s)
        dp = list(range(n))
        
        for mid in range(1, n):
            
            start = end = mid
            while start >= 0 and end < n and s[start] == s[end]:
                cut = 0 if start == 0 else dp[start - 1] + 1
                dp[end] = min(dp[end], cut)
                start -= 1
                end += 1
            
            start, end = mid - 1, mid
            while start >= 0 and end < n and s[start] == s[end]:
                cut = 0 if start == 0 else dp[start - 1] + 1
                dp[end] = min(dp[end], cut)
                start -= 1
                end += 1
        
        return dp[-1]
```


