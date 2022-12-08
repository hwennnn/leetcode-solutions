---
id: letter-case-permutation
title: Letter Case Permutation
description: Problem Description and Solution for Letter Case Permutation
sidebar_label: 784. Letter Case Permutation
sidebar_position: 784
---

# [784. Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)

```py title=letter-case-permutation.py
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        n = len(S)
        
        def backtrack(i, s):
            if i == n: 
                res.append("".join(s))
                return
            
            if s[i].isalpha():
                s[i] = s[i].upper()
                backtrack(i+1, s)
                
                s[i] = s[i].lower()
                backtrack(i+1, s)
            
            else:
                backtrack(i+1, s)
        
        backtrack(0, list(S))
        
        return res
```


