---
id: longest-string-chain
title: Longest String Chain
description: Problem Description and Solution for Longest String Chain
sidebar_label: 1048. Longest String Chain
sidebar_position: 1048
---

# [1048. Longest String Chain](https://leetcode.com/problems/longest-string-chain/)

```py title=longest-string-chain.py
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1
        
        for word in sorted(words, key = len):
            dp[word] = 1
            
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
                    res = max(res, dp[word])
        
        return res
```


