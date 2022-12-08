---
id: word-break
title: Word Break
description: Problem Description and Solution for Word Break
sidebar_label: 139. Word Break
sidebar_position: 139
---

# [139. Word Break](https://leetcode.com/problems/word-break/)

```py title=word-break.py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        
        for i in range(n):
            for word in wordDict:
                if s[i - len(word) + 1: i + 1] == word and (dp[i - len(word)] or i - len(word) == -1):
                    dp[i] = True
        
        return dp[-1]
```


