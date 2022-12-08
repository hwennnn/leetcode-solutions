---
id: shifting-letters-ii
title: Shifting Letters II
description: Problem Description and Solution for Shifting Letters II
sidebar_label: 2381. Shifting Letters II
sidebar_position: 2381
---

# [2381. Shifting Letters II](https://leetcode.com/problems/shifting-letters-ii/)

```py title=shifting-letters-ii.py
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        A = [ord(x) - ord('a') for x in s]
        B = [0] * (n + 1)
        
        for start, end, direction in shifts:
            c = 1 if direction == 1 else -1
            
            B[start] += c
            B[end + 1] -= c

        for i in range(1, len(B)):
            B[i] += B[i - 1]

        for index, (a, b) in enumerate(zip(A, B)):
            A[index] += b
            A[index] %= 26
            
        return "".join([chr(x + ord("a")) for x in A])
```


