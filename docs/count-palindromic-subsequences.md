---
id: count-palindromic-subsequences
title: Count Palindromic Subsequences
description: Problem Description and Solution for Count Palindromic Subsequences
sidebar_label: 2484. Count Palindromic Subsequences
sidebar_position: 2484
---

# [2484. Count Palindromic Subsequences](https://leetcode.com/problems/count-palindromic-subsequences/)

```py title=count-palindromic-subsequences.py
class Solution:
    def countPalindromes(self, s: str) -> int:
        M = 10 ** 9 + 7
        N = len(s)
        res = 0

        def build(words):
            dp = [[[0] * 10 for _ in range(10)] for _ in range(N)]
            cnt = [0] * 10

            for i in range(N):
                c = ord(words[i]) - ord("0")

                if i > 0:
                    for j in range(10):
                        for k in range(10):
                            dp[i][j][k] = dp[i - 1][j][k]
                            if k == c:
                                dp[i][j][k] += cnt[j]
                
                cnt[c] += 1

            return dp
        
        prefix, suffix = build(s), build(s[::-1])[::-1]

        for i in range(2, N - 2):
            for j in range(10):
                for k in range(10):
                    res += prefix[i - 1][j][k] * suffix[i + 1][j][k]
                    res %= M
        
        return res

                
```


