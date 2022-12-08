---
id: palindrome-partitioning
title: Palindrome Partitioning
description: Problem Description and Solution for Palindrome Partitioning
sidebar_label: 131. Palindrome Partitioning
sidebar_position: 131
---

# [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

```py title=palindrome-partitioning.py
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        
        def go(index, path):
            nonlocal res
            
            if index == n:
                res.append(path)    
                return
            
            for j in range(index, n):
                x = s[index : j + 1]
                
                if x == x[::-1]:
                    go(j + 1, path + [x])
        
        go(0, [])
        
        return res
```


