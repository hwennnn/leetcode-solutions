---
id: decoded-string-at-index
title: Decoded String at Index
description: Problem Description and Solution for Decoded String at Index
sidebar_label: 880. Decoded String at Index
sidebar_position: 880
---

# [880. Decoded String at Index](https://leetcode.com/problems/decoded-string-at-index/)

```py title=decoded-string-at-index.py
class Solution:
    def decodeAtIndex(self, S, K):
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
                
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1

```


