---
id: print-words-vertically
title: Print Words Vertically
description: Problem Description and Solution for Print Words Vertically
sidebar_label: 1324. Print Words Vertically
sidebar_position: 1324
---

# [1324. Print Words Vertically](https://leetcode.com/problems/print-words-vertically/)

```py title=print-words-vertically.py
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        m = len(max(words, key=len))
        n = len(words)
        res = ["" for _ in range(m)]
        
        for i,x in enumerate(words):
            for j in range(m):
                if j >= len(x):
                    res[j] += " "
                else:
                    res[j] += x[j]
        
        for i in range(m):
            res[i] = res[i].rstrip()
                
        
        return res
        
```


