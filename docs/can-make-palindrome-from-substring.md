---
id: can-make-palindrome-from-substring
title: Can Make Palindrome from Substring
description: Problem Description and Solution for Can Make Palindrome from Substring
sidebar_label: 1177. Can Make Palindrome from Substring
sidebar_position: 1177
---

# [1177. Can Make Palindrome from Substring](https://leetcode.com/problems/can-make-palindrome-from-substring/)

```py title=can-make-palindrome-from-substring.py
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        res = []
        dp = [[0] * 26]
        
        for i in range(1, n + 1):
            t = dp[i - 1][:]
            ch = ord(s[i - 1]) - ord('a')
            t[ch] += 1
            dp.append(t)
        
        
        for l,r,k in queries:
            left = dp[l]
            right = dp[r + 1]
            
            cnt = 0
            for i in range(26):
                cnt += (right[i] - left[i]) & 1
            
            res.append(cnt // 2 <= k)
        
        return res
```


