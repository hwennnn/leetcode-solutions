---
id: count-number-of-texts
title: Count Number of Texts
description: Problem Description and Solution for Count Number of Texts
sidebar_label: 2266. Count Number of Texts
sidebar_position: 2266
---

# [2266. Count Number of Texts](https://leetcode.com/problems/count-number-of-texts/)

```py title=count-number-of-texts.py
class Solution:
    def countTexts(self, A: str) -> int:
        n = len(A)
        M = 10 ** 9 + 7
        
        @cache
        def go(i):
            if i == n: return 1
            
            res = go(i + 1)
            z = 4 if A[i] in "79" else 3

            for k in range(i + 1, min(n, i + z)):
                if A[k] == A[i]:
                    res += go(k + 1)
                else:
                    break

                
            return res % M
        
        return go(0)
                
            
            
```


