---
id: decode-the-slanted-ciphertext
title: Decode the Slanted Ciphertext
description: Problem Description and Solution for Decode the Slanted Ciphertext
sidebar_label: 2075. Decode the Slanted Ciphertext
sidebar_position: 2075
---

# [2075. Decode the Slanted Ciphertext](https://leetcode.com/problems/decode-the-slanted-ciphertext/)

```py title=decode-the-slanted-ciphertext.py
class Solution:
    def decodeCiphertext(self, s: str, rows: int) -> str:
        n = len(s)
        cols = n // rows
        mat = [[" "] * cols for _ in range(rows)] 
        res = ""
        
        for i in range(n):
            mat[i // cols][i % cols] = s[i]
        
        for j in range(cols):
            i = 0
            res += mat[i][j]
            i += 1
            j += 1
            
            while i < rows and j < cols:
                res += mat[i][j]
                i += 1
                j += 1
        
        return res.rstrip()
```


